# thl_phonetic_transliteration

## Description
The goal of this code is to provide a library to convert Tibetan unicode and Wylie transliterations to THL Simplified Phonetic Transliteration.
This project was inspired by the similar Perl module created by Roger Espel Llima and the pyewts module for converting between Tibetan unicode
and Wylie transliterations.

This package is part of the larger MLotsawa project for machine translation of Literary Tibetan. The code for the entire project, 
including this package is [available on GitHub here.](https://github.com/billingsmoore/MLotsawa)

## Installation

```
pip install thl-phonetic-transliteration
```

## Examples

```python
from thl_phonetic_transliteration.converter import convert

tibetan_text = '<your Tibetan text>'

thl_phonetics = convert(tibetan_text)
```
## License

Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

## Owner

[@billingsmoore](https://github.com/billingsmoore)