# MLotsawa

## Introduction

This project is an attempt at creating user-friendly translation software to be used for translating from Literary Tibetan to English, with a particular focus on the literature of Tibetan Buddhism. The objective is to produce a tool which can assist (not replace!) human translators in the process of creating English language versions of the texts. 

The intended use case for this project is to be used locally on a reasonably priced computer of the kind that might be used by a non-specialist. The intended specifications for this imagined machine are 8 GB of RAM with no dedicated GPU. For example, an ideal product would be usable on a reasonably new MacBook Air or mid-price HP laptop.

In general, if you acquired your computer after 2020, you should be fine. If you have questions about your computer or have trouble running the app, please let me know.

For any questions or feedback, please email me at billingsmoore [at] gmail [dot] com with 'MLotsawa' in the subject line.

The code for the entire project is available in this repository, in [Notebooks](https://github.com/billingsmoore/MLotsawa/tree/main/Notebooks).
Documentation on the process of training and testing models can be found in [Docs](https://github.com/billingsmoore/MLotsawa/tree/main/Docs).

All models and datasets can be found on [Hugging Face](https://huggingface.co/billingsmoore)

## Getting Started

Currently, the suggested way of using this project is through the PyPI module, [mlotsawa](https://pypi.org/project/mlotsawa/). Instructions can be found at that link.

If you are not comforable working with Python modules, a demo version can be downloaded to run as a desktop app. Be aware that this version is substantially behind the PyPI module. You can try the demo on your own computer by downloading it from the link below. 

The demo currently expects input that has been transliterated into THL Simplified Phonetic Transliteration. It will accept input from unicode Tibetan Script or Wylie transliteration but, for now, performance is substantially worse. Right now, it also, in general, performs better on full lines or sentences than on single words.

If you have any trouble getting started please don't hesitate to contact me for help or to set up time for a one-on-one demo.

### Downloads

[You can download a version for Windows here.](https://drive.google.com/uc?export=download&id=1FTimh3FVE5JyvVnhWmglayiGMi3ohXHC)

[You can download a version for Linux here.](https://drive.google.com/uc?export=download&id=1qQlt5NN77WX0ox_Wgp9iBuTyC4tdFM7v)

## More Info

### Model Architecture

The architecture that was used for model training was Google's T5. The size used was the 'Large' model with 770 million parameters. The original model can be found on Huggingface as google-t5/t5-large. 

### Training Data

[The dataset for this project can be found here.](https://www.kaggle.com/datasets/billingsmoore/classical-tibetan-to-english-translation-dataset)

This dataset used for this project consists of pairs of sentences or phrases. The first member of each pair is a sentence or phrase in Classical Tibetan. The second member is the English translation of the first.

The pairs are pulled from texts sourced from [Lotsawa House](lotsawahouse.org). There was an initial set of over 15 million pairs.

The architecture selection process utilized a random subset of 100,000 pairs. A randomized 20,000 of which were used for evaluation.

The model size selection process utilized a larger random subset of 1 million pairs and a separate set of 100,000 pairs for evaluation.

The hyperparameter tuning process utilized a random subset of 10 million pairs and a seperate subset of 100,000 pairs for evaluation.

For final model training, the set of 1 million was reused for 6 epochs, then the 10 million pair set was used for 1 additional epoch.

### Example Translation

For an example translation, we can use 'A Brief Amitabha Sleeping Practice' by Jamyang Khyentse Chökyi Lodrö. I've provided a translation of the first two verses of the text side by side with Adam Pearcey's original translation.

This text was selected because the translation does not preserve any Tibetan terms (which is sometimes intentionally done by translators for the sake of technical or philosophical specificity) but does include a handful of Sanksrit words (i.e. Buddha, Dharma) which have been adopted into English and are extremely common in the corpus. Additionally, it is not considered a restricted, or secret, text which is sometimes the case with important texts within the tradition.

| Pearcey | MLotsawa |
|---------|----------|
|***In the Buddha the Dharma and the Supreme Assembly<br>I take refuge until I attain enlightenment<br>Through the merit of practising generosity and so on<br>May I attain buddhahood for the benefit of all beings***|***in the buddha the dharma and the supreme assembly<br>i take refuge till enlightenment is realized<br>through the merit of practising generosity and so on<br>may i attain buddhahood for the benefit of all beings***|
|***You are the protectors of all beings every single one<br>You are the deities who remorselessly destroy the maras and their forces<br>You who know all things just as they are in their true nature<br>Enlightened ones with your retinues come now to this place***|***you are the protector of all beings without exception<br>are the deities who remorselessly destroy the mras and their forces<br>you who know all things just as they are in their true nature<br>i pray that the buddhas with their retinues come now to this place***|

## Further Documentation

More documentation about this project can be found in the 'Docs' folder of this project. I recommend starting with ['Translation Model Over'](https://github.com/billingsmoore/MLotsawa/blob/main/Docs/TranslationModelOverview.md)
