# Dataset Card for OCR-Betsug

A line-to-text dataset for Tibetan OCR of the Betsug script.

## Dataset Details

### Dataset Description
- **Curated by:** Buddhist Digital Resource Center
- **Language:** Tibetan
- **Total Samples:** 28,318 line images with text transcriptions

### Dataset Structure
- **Features:**
  - `id`: Image file identifier
  - `image`: Image file of text
  - `label`: Text transcription

- **Splits:**
  - **Train:** 28,318 samples

## Uses

### Direct Use
- Training and evaluation of Tibetan OCR models
- Betsug (or other Ume) script OCR development
- Comparative analysis of historical scripts
- Large-scale OCR model pretraining

### Out-of-Scope Use
- Not be suitable for printed Tibetan texts or Uchen script
- May not suitably represent contemporary digital Tibetan fonts

## Dataset Creation

### Curation Rationale and Process
This dataset was created from 2 manuscripts to support the development of robust OCR systems for Tibetan literature, including handwritten material.


## Usage

```python
from datasets import load_dataset

# Load training split
dataset = load_dataset("openpecha/OCR-Betsug", split="train")

# Example features
print(dataset[0])
# {'id': 'I1KG812780077_1', 
# 'image': <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=2133x52 at 0x7B784AD93860>, 
# 'label': 'ཀྱི་ཐིག་ལེ་ཏེ་།   རྟེན་དང་བརྟེན་པར་བཅས་པ་ཉིད་།  རང་ཉིད་གསལ་བར་བྱིན་བརླབས་ན་།  ཇི་ལྟར་སྣང་སྲིད་ཆོས་ཐམས་ཅད་།   ལྷན་ཅིག་སྐྱེས་པའི་ངོ་བོར་'}
```

## Dataset Contact
BDRC - help@bdrc.org