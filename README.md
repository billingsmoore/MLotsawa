# MLotsawa

This project is an attempt at creating user-friendly translation software to be used for translating 
from Classical Tibetan to English. 

## Introduction

## Data

The dataset for this project can be found here: 
https://www.kaggle.com/datasets/billingsmoore/classical-tibetan-to-english-translation-dataset/data

This dataset consists of 100,000 pairs of sentences or phrases. The first member of each pair is a sentence or phrase in Classical Tibetan. The second member is the English translation of the first.

The pairs are pulled from texts sourced from Lotsawa House (lotsawahouse.org) and are offered under the same license as the original texts they provided.

The data is provided as a pickled pandas data frame which consists of a single column, 'translation'. Entries in that column are a python dictionary of the structure: {'bo': 'Tibetan text', 'en': 'English text'}.

The purpose of this structure is to mimic the OPUS books dataset which is popular in machine translation tutorials and therefore be easily usable with code that was originally intended to work with that dataset.
