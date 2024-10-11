# MLotsawa

## Introduction

This project is an attempt at creating user-friendly translation software to be used for translating from Literary Tibetan to English, with a particular focus on the literature of Tibetan Buddhism. The objective is to produce a tool which can assist (not replace!) human translators in the process of creating English language versions of the texts. 

The intended use case for this project is to be used locally on a reasonably priced computer of the kind that might be used by a non-specialist. The intended specifications for this imagined machine are 8 GB of RAM with no dedicated GPU. For example, an ideal product would be usable on a reasonably new MacBook Air or mid-price HP laptop.

In general, if you acquired your computer after 2020, you should be fine. If you have questions about your computer or have trouble running the app, please let me know.

For any questions or feedback, please email me at billingsmoore [at] gmail [dot] com with 'MLotsawa' in the subject line.

The code for this project is available in in [Notebooks](https://github.com/billingsmoore/MLotsawa/tree/main/Notebooks).

Documentation on the process of training and testing models can be found in [Docs](https://github.com/billingsmoore/MLotsawa/tree/main/Docs).

All models and datasets can be found on [Hugging Face](https://huggingface.co/billingsmoore)

## Getting Started

Currently, the suggested way of using this project is through the PyPI module, [mlotsawa](https://pypi.org/project/mlotsawa/). Instructions can be found at that link.

If you are not comfortable working with Python modules, a demo version can be downloaded to run as a desktop app. Be aware that this version is substantially behind the PyPI module. You can try the demo on your own computer by downloading it from the link below. 

The demo currently expects input that has been transliterated into THL Simplified Phonetic Transliteration. It will accept input from unicode Tibetan Script or Wylie transliteration but, for now, performance is substantially worse. Right now, it also, in general, performs better on full lines or sentences than on single words.

If you have any trouble getting started please don't hesitate to contact me for help or to set up time for a one-on-one demo.

### Downloads

[You can download a version for Windows here.](https://drive.google.com/uc?export=download&id=1FTimh3FVE5JyvVnhWmglayiGMi3ohXHC)

[You can download a version for Linux here.](https://drive.google.com/uc?export=download&id=1qQlt5NN77WX0ox_Wgp9iBuTyC4tdFM7v)
