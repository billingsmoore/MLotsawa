# Dataset Card for KhyentseWangpo

A line-to-text dataset for Tibetan OCR.

## Dataset Details

### Dataset Description

This dataset consists of 13,527 rows with three columns: 

- `id` (string): Unique identifier for each line
- `image` (image): Image file containing a line of Tibetan text
- `transcription` (string): Tibetan text transcription in Unicode format

The dataset was created as part of the [BDRC](www.bdrc.io) - [MonlamAI](monlam.ai) OCR Project (B-MOP).

- **Curated by:** Buddhist Digital Resource Center & Monlam AI
- **Language:** Tibetan
- **License:** Open Data Commons Attribution License (ODC-By) v1.0

## Uses

### Direct Use

This dataset is intended for:
- Training and evaluating Tibetan Optical Character Recogntion (OCR) models
- Fine-tuning existing OCR systems for classical Tibetan texts
- Benchmarking line-level text recognition performance on Tibetan scripts
- Research on historical Tibetan document digitization

The dataset is particularly suited for models working with modern printed Tibetan text.

### Out-of-Scope Use

This dataset may not be suitable for:
- Handwritten Tibetan text recognition (as it contains modern printed text)
- Ancient manuscript OCR (different printing styles and conditions)
- General-purpose Tibetan language modeling without OCR context


## Dataset Creation

### Curation Rationale

This dataset was created to support the development of accurate OCR systems for Tibetan texts, particularly for digitizing the corpus of Tibetan Buddhist literature. The Collected Works of Jamyang Khyentse Wangpo (1820-1892), a prominent Tibetan Buddhist teacher and scholar, represents an important corpus of Tibetan religious and philosophical literature. Digitizing such works makes them more accessible to scholars, practitioners, and researchers worldwide.

### Source Data

The source material consists of [a modern print edition of the Collected Works (Sungbum) of Jamyang Khyentse Wangpo](http://purl.bdrc.io/resource/MW3PD1002). The data collection process involved:

1. **PDF Extraction**: Text was extracted from PDFs using the code found here: https://github.com/buda-base/py-tiblegenc
2. **Alignment**: The extracted text was aligned with BDRC scans of the same publication to ensure accuracy
3. **Line Segmentation**: The text was segmented into individual lines (13,524 total) for line-level OCR training
4. **Image-Text Pairing**: Each line of text was paired with its corresponding image segment


### Personal and Sensitive Information

This dataset contains no personal or sensitive information.

## Dataset Card Author

Jacob Moore (@billingsmoore)

billingsmoore [at] gmail [dot] com