# Dataset Card for OCR-LhasaKanjur

A line-to-text dataset for Tibetan OCR.

## Dataset Details

### Dataset Description
- **Curated by:** Buddhist Digital Resource Center
- **Language:** Tibetan
- **Total Samples:** 161,309 line images with text transcriptions

### Dataset Structure
- **Features:**
  - `id`: Image file identifier
  - `image`: Image of a line of text
  - `label`: Text transcription

- **Splits:**
  - **Train:** 130,109 samples
  - **Eval:** 14,877 samples  
  - **Test:** 16,326 samples (4.7M characters)

## Uses

### Direct Use
- Training and evaluation of Tibetan OCR models
- Multi-script OCR development
- Large-scale OCR model pretraining

### Out-of-Scope Use
- Not be suitable for handwritten Tibetan texts
- May not suitably represent contemporary digital Tibetan fonts

## Dataset Creation

### Curation Rationale and Process
This dataset was created to support the development of robust OCR systems for Tibetan literature, encompassing both modern typography and traditional woodblock printing methods. The inclusion of multiple scripts and printing techniques makes it valuable for training models that can handle diverse Tibetan textual sources.

The dataset is made up of material from a woodblock print edition of the Lhasa Kangyur.

## Usage

```python
from datasets import load_dataset

# Load training split
dataset = load_dataset("openpecha/OCR-Google_Books", split="train")

# Example features
print(dataset[0])
# {'id': '1-1-3b_0', 
# 'image': <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=1421x54 at 0x767F563BEF00>, 
# 'label': 'བ་དེའི་ཚེ་ན། དེས་ཀྱང་དཔུང་གི་ཚོགས་ཡན་ལག་བཞི་པ། གླང་པོ་ཆེ་པའི་ཚོགས་དང༌། རྟ་པའི་ཚོགས་དང༌། ཤིང་རྟ་པའི་ཚོགས་དང༌། དཔུང་བུ་ཆུང་གི་ཚོགས་གོ་བསྐོན་ཏེ། ཡུལ་ཨང་ག་ཙམ་'}

```

## Dataset Contact
BDRC - help@bdrc.org