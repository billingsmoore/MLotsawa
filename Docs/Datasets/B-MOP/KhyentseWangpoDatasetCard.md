# Dataset Card for KhyentseWangpo

A line-to-text dataset for Tibetan OCR.

## Dataset Details

### Dataset Description

This dataset consists of 13,527 rows with three columns: 

- `id` (string): Unique identifier for each line
- `image` (image): Image file containing a line of Tibetan text
- `transcription` (string): Tibetan text transcription in Unicode format

- **Curated by:** Buddhist Digital Resource Center 
- **Language:** Tibetan
- **License:** Open Data Commons Attribution License (ODC-By) v1.0

## Uses

### Direct Use

Training and evaluation of Tibetan OCR models, particularly for line-level recognition of modern printed texts.

### Out-of-Scope Use

Not suitable for handwritten manuscripts, historical woodblock prints, or other printing styles significantly different from modern Tibetan typography.

## Dataset Creation

### Curation Rationale

This dataset was created to support the development of accurate OCR systems for Tibetan texts, particularly for digitizing the corpus of Tibetan Buddhist literature. The Collected Works of Jamyang Khyentse Wangpo (1820-1892), a prominent Tibetan Buddhist teacher and scholar, represents an important corpus of Tibetan religious and philosophical literature. Digitizing such works makes them more accessible to scholars, practitioners, and researchers worldwide.

### Source Data

The source material consists of a modern print edition of the Collected Works (Sungbum) of Jamyang Khyentse Wangpo:

> Jamyang Khyentse Wangpo. (2014). gSung ʼbum mkhyen brtseʼi dbang po (Vol. 1–25). rDzong sar blo gros phun tshogs. http://purl.bdrc.io/resource/MW3PD1002 [BDRC bdr:MW3PD1002]



The data collection process involved:
1. **PDF Extraction**: Text was extracted from PDFs using the code found here: https://github.com/buda-base/py-tiblegenc
2. **Alignment**: The extracted text was aligned with BDRC scans
3. **Line Segmentation**: The scanned images and text were segmented into individual lines (13,524 total) for line-level OCR training
4. **Image-Text Pairing**: Each line of text was paired with its corresponding image segment

### Personal and Sensitive Information

This dataset contains no personal or sensitive information.

## Dataset Contact

help@bdrc.io