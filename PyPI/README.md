# mlotsawa

## Description

The purpose of this module is user-friendly translation and transliteration of Classical Tibetan. 

Currently, separate classes are provided for translation and transliteration tasks. Both classes will accept either a list of strings,
or a single string. The output of each will be of the same type as the input.

You can also run the translator and transliteration functions through a web-based user interface. The web interface will open automatically
when you use the code below.

Under the hood, this module uses the T5 transformer architecture, custom fine-tuned on data
from [Lotsawa House](www.lotsawahouse.org).

The models and datasets used by this project can be found on [Hugging Face](https://huggingface.co/billingsmoore) where you can find more
information on training, data collection, and how to use these models and datasets for your own projects.

This module is part of the larger MLotsawa project for machine translation of Literary Tibetan. The code for the entire project, 
including this module is [available on GitHub here.](https://github.com/billingsmoore/MLotsawa)

## Installation

```
pip install --upgrade mlotsawa
```

## Examples

For transliteration:

```python
from mlotsawa.transliterator import Transliterator 

tibetan_text = '<your Tibetan text>'

transliterator = Transliterator()

phonetics = transliterator.transliterate(tibetan_text)
```

For translation:

```python
from mlotsawa.translator import Translator 

tibetan_text = '<your Tibetan text>' # may be in Tibetan script or phoneticized

translator = Translator()

translation = translator.translate(tibetan_text)
```

To server Web based user-interface:

```python
from mlotsawa.webui import WebUI

webui = WebUI()

webui.run()
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