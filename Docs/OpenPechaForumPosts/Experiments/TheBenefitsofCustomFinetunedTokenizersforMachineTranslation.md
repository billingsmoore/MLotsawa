# The Benefits of Custom Finetuned Tokenizers for Machine Translation

## Introduction

In order for language models to process text, that text must first be "tokenized". This means that the text is converted into a sequence of numbers ("tokens") that can be used for the linear algebraic calculations performed by the model. This tokenization process typically maps words, characters, or common groups of characters to a given integer.

Tokenization, for most large language models, is performed by a Sentence Piece model which has been trained on a large dataset of raw text. These tokenizers can generally be used with no additional training or finetuning for most text processing tasks. 

However, the training data for these tokenizers is generally heavily biased in favor of English or other Western languages which use the Latin alphabet. As a result, these tokenizers generally do not handle text well if it is written in non-Latin scripts. In the best case scenario, the tokenizers recognize only a small number of characters from a given script, and in the worst case scenario, they treat every piece of text in a given script as an "unknown" token.

T5 is a language model designed for text-to-text generative tasks, like machine translation, produced by Google. It is often treated as the default standard for text processing in machine learning, and anecdotally, has produced relatively encouraging results in applications to the Tibetan language. However, the tokenizer used for the T5 language model does not natively support any Tibetan text.

For example, using the tokenizer for T5-small, tokenizing the text: བླ་མ་དང་ལྷག་པའི་ལྷ་ལ་ཕྱག་འཚལ་ལོ།།

Produces the following numerical sequence: [3, 2, 1]

Which, when decoded by the same tokenizer produces: \<unk>\</s>

Here, "\<unk>" represents an unknown token, and "\</s>" represents the end of a string. Thus, the tokenizer has simply treated the entire input text as an unknown. 

The simplest remedy for this situation is to just add the characters used in the Tibetan script to the tokenizer. This increases the vocabulary of the tokenizer, and the input layer of the associated model must be resized, but there is otherwise no real obstacle to this approach. This can be done quickly and easily with the following code block:

```python
# Load the tokenizer and model from Hugging Face
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google-t5/t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Generate a list of all Tibetan Unicode characters (U+0F00 to U+0FFF)
tibetan_chars = [chr(codepoint) for codepoint in range(0x0F00, 0x0FFF)]

# Add new tokens to the tokenizer
tokenizer.add_tokens(tibetan_chars)

# Resize model embeddings to accommodate the new vocabulary size
model.resize_token_embeddings(len(tokenizer))
```

Once this has been performed, the tokenizer now handles Tibetan text more gracefully.

For example, using the tokenizer for T5-small, tokenizing the text: བླ་མ་དང་ལྷག་པའི་ལྷ་ལ་ཕྱག་འཚལ་ལོ།།

Produces the following numerical sequence: [32186, 32279, 32111, 32188, 32111, 32181, 32168, 32111, 32199, 32283, 32166, 32111, 32184, 32196, 32214, 32111, 32199, 32283, 32111, 32199, 32111, 32185, 32277, 32166, 32111, 32196, 32190, 32199, 32111, 32199, 32224, 32113, 32113, 1]

Which, when decoded by the same tokenizer produces: བླ་མ་དང་ལྷག་པའི་ལྷ་ལ་ཕྱག་འཚལ་ལོ།།\</s>

You can see that the output of the tokenizer after decoding is identical to the input prior to encoding except for the addition of the explicit end of string token.

However, you can also see that the numerical sequence is quite long. This can be a detriment to text processing, where the length of input and output strings is often limited to a certain number of tokens (often 256, or 512).

It is thus worth investigating if there is any benefit in going the extra mile to custom finetune a tokenizer.

## Hypothesis and Description of Experiments

I suggest the following two hypotheses, finetuning a custom tokenizer will (1) reduce the length of encoded inputs (allowing for processing of longer input strings) and (2) produce better results on standard model metrics.

I take the hypotheses to be supported if (1) the average length of tokenized inputs is shorter for the custom finetuned tokenizer and (2) the machine translations of the model which uses the custom finetuned tokenizer are of higher quality, as measured by [BLEU](https://en.wikipedia.org/wiki/BLEU) and [chrF](https://machinetranslate.org/chrF) scores, respectively.

I will thus run two experiments. In the first ("Experiment 1") I will tokenize a set of Tibetan text using a tokenizer to which I have simply added all of the unicode characters of the Tibetan script to the tokenizer (as in the Introduction section above) and then tokenize those texts again using a custom fine-tuned tokenizer. I will then compare the mean lengths of the tokenized encodings.

In the second ("Experiment 2"), I will train two T5 models for machine translation from Tibetan to English, one using a tokenizer to which I have simply added all of the unicode characters of the Tibetan script to the tokenizer (as in the Introduction section above) and the other using a custom fine-tuned tokenizer.

For both experiments, the dataset used is '[billingsmoore/tibetan-to-english-translation-dataset](https://huggingface.co/datasets/billingsmoore/tibetan-to-english-translation-dataset)'. This dataset consists of three columns, the first of which is a sentence or phrase in Tibetan, the second is the phonetic transcription of the Tibetan, and the third is the English translation of the Tibetan, though the phonetics were not used for either experiment. The dataset was scraped from Lotsawa House and is known to be very clean. The dataset has ~81,000 samples. Every sample is used for Experiment 1, but only a subset of 25,500 training samples is used for Experiment 2, with 4,500 set aside as test data.

## Experiment Results

### Experiment 1

In Experiment 1, the tokenizer to which all Tibetan characters were added individually resulted in a mean encoded input length of **37.768** tokens. The tokenizer which was custom finetuned resulted in a mean encoded input length of **4.650** tokens, a change of **-87.69%** in mean encoded input length.

### Experiment 2

The training results of Experiment 2 are shown in the graphs below. The model trained using the custom finetuned tokenizer ("custom-finetuned") significantly outperforms the model using the tokenizer to which the Tibetan characters have been added individually ("just-add") in both BLEU (Figure 1) and chrF (Figure 2).

![Bleu Results](custom-tokenizer-bleu.png)
*Figure 1: BLEU Scores*

![chrF Results](custom-tokenizer-chrf.png)
*Figure 2: chrF Scores*

## Discussion

Custom finetuning the tokenizer for T5 results in both much shorter encoded input lengths and higher quality machine translation results. 

The only downside to a custom finetuned tokenizer, in my experience, is the additional training time. However, for these experiments, adding the characters individually took 1.8 seconds, while finetuning the tokenizer using the SentecePiece train_from_iterator method took 4.6 seconds. While this assumes a relatively small set of training data, it seems unlikely that custom finetuning constitutes a meaningful obstacle in terms of time for most use-cases.

Thus, when possible, a custom finetuned tokenizer should be used for machine translation of Tibetan with T5 models.