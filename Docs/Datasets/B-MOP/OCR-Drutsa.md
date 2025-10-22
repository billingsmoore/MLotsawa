# Dataset Card for OCR-Drutsa

A line-to-text dataset for Tibetan OCR of the Drutsa script.

## Dataset Details

### Dataset Description
- **Curated by:** Buddhist Digital Resource Center
- **Language:** Tibetan
- **Total Samples:** 32,364 line images with text transcriptions

### Dataset Structure
- **Features:**
  - `id`: Image file identifier
  - `image`: Image file of text
  - `label`: Text transcription

- **Splits:**
  - **Train:** 32,364 samples

## Uses

### Direct Use
- Training and evaluation of Tibetan OCR models
- Drutsa script OCR development
- Comparative analysis of historical scripts
- Large-scale OCR model pretraining

### Out-of-Scope Use
- Not be suitable for printed Tibetan texts or Uchen script
- May not suitably represent contemporary digital Tibetan fonts

## Dataset Creation

### Curation Rationale and Process
This dataset was created from 10 manuscripts to support the development of robust OCR systems for Tibetan literature, including handwritten material.


## Usage

```python
from datasets import load_dataset

# Load training split
dataset = load_dataset("openpecha/OCR-Drutsa", split="train")

# Example features
print(dataset[0])
# {'id': 'KS_11-061_line_9874_4', 
# 'image': <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=2335x82 at 0x7ED68C896600>, 
# 'label': 'བས་སོ་། །༢པ་ཡང་མི་འཐད་ཏེ་སྣལ་མ་དུ་མ་འདུས་པ་ལས་འབྲས་བུ་སྣམ་པུ་ཡོད་ན་སྣལ་མ་སོ་སོ་ལ་འབྲས་བུ་ཆ་རི་དམིགས་པར་ཐལ་ལོ་། །དེས་ན་སྣལ་'}
```

## Dataset Contact
BDRC - help@bdrc.org