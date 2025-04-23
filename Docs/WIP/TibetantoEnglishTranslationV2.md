# Tibetan to English Translation v2

## Notes to self

initial training with full dataset gave unsatisfactory results, training data was thus restricted to Buddhist material

test runs with gradient clipping and label smoothing seemed to diminsh performance so finetuning was started without them

finetuning with a longer max epoch size accidentally produces slower decay in the optimizer, which improved performance significantly

finetuning of the small model crashed after 36 epochs, and restarted

## Custom Tokenizer

From **The Benefits of Custom Finetuned Tokenizers for Machine Translation**:

    In order for language models to process text, that text must first be "tokenized". This means that the text is converted into a sequence of numbers ("tokens") that can be used for the linear algebraic calculations performed by the model. This tokenization process typically maps words, characters, or common groups of characters to a given integer.

    Tokenization, for most large language models, is performed by a Sentence Piece model which has been trained on a large dataset of raw text. These tokenizers can generally be used with no additional training or finetuning for most text processing tasks. 

    However, the training data for these tokenizers is generally heavily biased in favor of English or other Western languages which use the Latin alphabet. As a result, these tokenizers generally do not handle text well if it is written in non-Latin scripts. In the best case scenario, the tokenizers recognize only a small number of characters from a given script, and in the worst case scenario, they treat every piece of text in a given script as an "unknown" token.

    T5 is a language model designed for text-to-text generative tasks, like machine translation, produced by Google. It is often treated as the default standard for text processing in machine learning, and anecdotally, has produced relatively encouraging results in applications to the Tibetan language. However, the tokenizer used for the T5 language model does not natively support any Tibetan text.

    For example, using the tokenizer for T5-small, tokenizing the text: བླ་མ་དང་ལྷག་པའི་ལྷ་ལ་ཕྱག་འཚལ་ལོ།།

    Produces the following numerical sequence: [3, 2, 1]

    Which, when decoded by the same tokenizer produces: \<unk>\</s>

    Here, "\<unk>" represents an unknown token, and "\</s>" represents the end of a string. Thus, the tokenizer has simply treated the entire input text as an unknown. 

Custom finetuning the tokenizer for T5 results in both much shorter encoded input lengths and higher quality machine translation results.

In my previous experiments, the tokenizer to which all Tibetan characters were added individually resulted in a mean encoded input length of **37.768** tokens. The tokenizer which was custom finetuned resulted in a mean encoded input length of **4.650** tokens, a change of **-87.69%** in mean encoded input length.

Additionally, a model trained using the custom finetuned tokenizer ("custom-finetuned") significantly outperforms the model using the tokenizer to which the Tibetan characters have been added individually ("just-add") in both BLEU (Figure 1) and chrF (Figure 2).

## Continued Pretraining



## Finetuning