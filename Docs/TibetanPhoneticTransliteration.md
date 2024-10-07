# Tibetan Phonetic Transliteration

The purpose of this file is to document the process of creating the model ['billingsmoore/tibetan-phonetic-transliteration'](https://huggingface.co/billingsmoore/tibetan-phonetic-transliteration).

The model card for that model including a more formal explanation of its creating process and instructions for usage can be found at the link above.

The section headings below can be clicked to see the associated Jupyter notebook.

## [An Attempt at a Classical Approach](../Notebooks/Models/TibetanPhoneticTransliteration/ClassicalApproach.ipynb)

Initially, it was hoped that a machine learning model would not be necessary for transliteration. The original implementation of transliteration for 
this project utilized a classical algorithm inspired by the Perl module created by Roger Espel Llima and available on [The Tibetan & Himalayan Library website here](https://www.thlib.org/reference/transliteration/phconverter.php).

Difficulties with this approach suggested that relying on an initial transliteration according to the Wylie standard may be useful. From there, the Wylie could be converted into phonetics. In particular, it was hoped that this might accomodate the ambiguous breaking of words in writtern Tibetan. To accomplish this, the [PyEWTS Python module](https://pypi.org/project/pyewts/) was used. Unfortunately, this approach also proved more difficult than expected and consistently produced less than desirable results.

Thus, the decision was made to instead implement a Transformer based solution.

## [T5 Model](/Notebooks/Models/TibetanPhoneticTransliteration/TibetanPhoneticTransliteration.ipynb)

### Poor Beginnings

The base model for transliteration is Google's T5-small architecture. It was finetuned for 32 epochs with a learning rate of 3e-4 on a dataset of 98,597 pairs of Tibetan script with its phonetic transliteration. This set was scraped and structured programmatically from [Lotsawa House](lotsawahouse.org).

The final evaluation loss during training was 1.01475. The graph of training results can be seen below.

![Training Results](readme-assets/transliteration/transliteration-training-results.png?raw=true "Graph of training results")

However, this model, even after just a single epoch, outputs the same sequence for every input. This may be a result of any overly high learning rate or of problems in tokenizing the Tibetan unicode.

To address this problem, the model was first retrained with a learning rate of 2e-5. Then, the model was trained with input and output texts tokenized at the character level. The results of the first five epochs of training for each experiment can be seen below. Note that, initially, the loss curves are roughly identical for both approaches when learning rates are the same. However, the single character tokenizations level off more quickly and final evaluation losses are worse.

![Transliteration Experiment Results](readme-assets/transliteration/transliteration-experiments.png?raw=true "Graph of training results")

The lower learning rate on its own did not resolve the problem of producing identical (incorrect) outputs for every input, nor did the altered approach to tokenization.

### Solving Tokenizer Problems

Further investigation found that the t5 tokenizer was not encoding the original Tibetan characters properly, even when those characters were encoded individually.

To address this issue, Tibetan character were specifically added to the tokenizer, and the model was resized to accomadate the changed dimensionality of inputs. 
The code used for that process can be found in the associated notebook.

The adjusted base model was then trained for 5 epochs. The results of training with that tokenizer can be seen below.

![Altered Tokenizer Results](readme-assets/transliteration/altered-tokenizer-results.png?raw=true "Graph of training results with the altered tokenizer")

Outputs from this model are of acceptably high quality.