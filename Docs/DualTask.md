# Dual Task Model (Oct 11, 2024)

## Objective

The objective of the dual task model is to create a single model that can effectively provide both transliteration and translation.

The current (Oct 12, 2024) implementation of MLotsawa relies on two different models, which creates two problems. The first is that two models must be downloaded and held in memory. This may be prohibitively computationally intensive for some users.

The second issue is that only one model can be effectively loaded onto a GPU at a time. This means that at least one model (currently the transliteration model) must be run on CPU, which is much slower.

## Training

As a proof of concept, the [T5-small model](https://huggingface.co/google-t5/t5-small) was fine-tuned on
['billingsmoore/tibetan-to-english-translation-dataset'](https://huggingface.co/datasets/billingsmoore/tibetan-to-english-translation-dataset).

The model tokenizer was extended to allow for Tibetan script. Then, the dataset was split to create source-target pairs of both Tibetan-English and Tibetan-Phonetic pairs. These were tokenized and then concatenated into a single dataset for training. The fine-tuned model was evaluated by Loss and BLEU scores.

Graphs of training results can be seen below.

![Losses](readme-assets/dual-task/dual-task-loss.png?raw=true "Graph of losses")

![BLEU](readme-assets/dual-task/dual-task-bleu.png?raw=true "Graph of BLEU scores")

Note that the model was evaluated on the combined test set of both translation and transliteration pairs and thus, results may not be reliably indicative of translation quality, only that quality continued to improve on the combined tasks over the course of training.

## Conclusion

These results are taken to be encouraging and henceforth, models will be trained to perform both transliteration and translation with a single model. Thus, the next phase of models will be trained to translate from Tibetan script or phoneticized Tibetan, and to transliterate from Tibetan script into phoneticized Tibetan.