# Dataset Card for OCR-Google_Books

A line-to-text dataset for Tibetan OCR.

## Dataset Details

### Dataset Description
- **Curated by:** Buddhist Digital Resource Center
- **Language:** Tibetan
- **Total Samples:** 751,456 line images with text transcriptions

### Dataset Structure
- **Features:**
  - `id`: Image file identifier
  - `label`: Text transcription
  - `url`: Source URL of the original document

- **Splits:**
  - **Train:** 601,152 samples (37.3M characters)
  - **Eval:** 75,136 samples (4.7M characters)  
  - **Test:** 75,168 samples (4.7M characters)

## Uses

### Direct Use
- Training and evaluation of Tibetan OCR models
- Multi-script OCR development
- Comparative analysis of modern vs. traditional printing methods
- Large-scale OCR model pretraining

### Out-of-Scope Use
- Not be suitable for handwritten Tibetan texts
- May not suitably represent contemporary digital Tibetan fonts

## Dataset Creation

### Curation Rationale and Process
This dataset was created to support the development of robust OCR systems for Tibetan literature, encompassing both modern typography and traditional woodblock printing methods. The inclusion of multiple scripts and printing techniques makes it valuable for training models that can handle diverse Tibetan textual sources.

The dataset is constructed from Google Books scans of Tibetan texts, with Line-level image-text pairs extracted from scanned pages

## Usage

```python
from datasets import load_dataset

# Load training split
dataset = load_dataset("openpecha/OCR-Google_Books", split="train")

# Example features
print(dataset[0])
# {'id': 'I1KG1163750042_0025',
#'label':'ཡིན་པས་ཆབ་སྲིད་དང་འབྲེལ་བ་བྱུང་བ་ཙམ་ལ་ངོ་མཚར་དགོས་དོན་གང་',
# 'url': 'https://s3.amazonaws.com/monlam.ai.ocr/OCR/training_images/I1KG1163750042_0025.jpg'}
```

## Dataset Contact
BDRC - help@bdrc.org