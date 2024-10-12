# Dual Task Model

## Objective

The objective of the dual task model is to create a single model that can effectively provide both transliteration and translation.

The current (Oct 12, 2024) implementation of MLotsawa relies on two different models, which creates two problems. The first is that two models must be downloaded and held in memory. This may be prohibitively computationally intensive for some users.

The second issue is that only one model can be effectively loaded onto a GPU at a time. This means that at least one model (currently the transliteration model) must be run on CPU, which is much slower.

