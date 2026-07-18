# MLotsawa

> **Note:** This repo is in the middle of a significant reorganization. Several bodies of work that
> had accumulated here (dataset creation, OCR, embedding models, ASR experiments, domain tagging,
> individual papers, etc.) are being split out into their own focused repos — see
> [Related Repositories](#related-repositories) below. Expect continued restructuring; some docs and
> links may be in flux until this settles.

## Introduction

This project is an attempt at creating user-friendly translation software to be used for translating from Literary Tibetan to English, with a particular focus on the literature of Tibetan Buddhism. The objective is to produce a tool which can assist (not replace!) human translators in the process of creating English language versions of the texts. 

The intended use case for this project is to be used locally on a reasonably priced computer of the kind that might be used by a non-specialist. The intended specifications for this imagined machine are 8 GB of RAM with no dedicated GPU. For example, an ideal product would be usable on a reasonably new MacBook Air or mid-price HP laptop.

In general, if you acquired your computer after 2020, you should be fine. If you have questions about your computer or have trouble running the app, please let me know.

For any questions or feedback, please email me at billingsmoore [at] gmail [dot] com with 'MLotsawa' in the subject line.

The code for this project is available in [Notebooks](https://github.com/billingsmoore/MLotsawa/tree/main/Notebooks).

Documentation on the process of training and testing models can be found in [Docs](https://github.com/billingsmoore/MLotsawa/tree/main/Docs).

All models and datasets created and used by this project can be found on [Hugging Face](https://huggingface.co/billingsmoore)

If you are interested in the research aspect of this project, I suggest reading [Validating Retrieval Augmented Translation With T5](Docs/Experiments/ValidatingRetrievalAugmentedTranslationWithT5.md) or [Knowledge Graphs for Accessible Machine Generated Translations and Commentaries](https://github.com/billingsmoore/openpecha-forum-posts/blob/main/KnowledgeGraphs/KnowledgeGraphsforAccessibleMachineGeneratedTranslationsandCommentaries.md)

## Getting Started

The previous PyPI module and WordPress/React integrations have been deprecated and removed from this
repository. For now, the easiest way to try translation is
[SimpleTranslationUI](https://huggingface.co/spaces/billingsmoore/SimpleTranslationUI), a free
Hugging Face Space with a graphical editor for translating `.txt`, `.docx`, and `.pdf` documents
(source on [GitHub](https://github.com/billingsmoore/SimpleTranslationUI)). It runs on
`mlotsawa-ground-base` by default, or an OpenRouter model of your choice if you provide an API key.

If you have any trouble getting started please don't hesitate to contact me for help or to set up time for a one-on-one demo.

## Related Repositories

Work that used to live in this repo, or that this repo's models feed into downstream, now lives in
its own place:

**Applications**
- [SimpleTranslationUI](https://github.com/billingsmoore/SimpleTranslationUI) — the graphical
  translation editor described above

**This paper's code**
- [optimizing-t5-tibetan-english-mt](https://github.com/billingsmoore/optimizing-t5-tibetan-english-mt) —
  training/ablation/eval code for *Optimizing T5 for Lightweight Tibetan-English Translation*
  ([preprint](https://doi.org/10.21203/rs.3.rs-7409829/v1)), which produced the
  `mlotsawa-ground-small`/`-base` models

**Dataset creation/curation**
- [tibetan-translation-datasets](https://github.com/billingsmoore/tibetan-translation-datasets) —
  Tibetan-English translation dataset creation, cleaning, and formatting
- [bdrc-ocr-datasets](https://github.com/billingsmoore/bdrc-ocr-datasets) — BDRC-curated Tibetan OCR
  dataset notebooks and dataset cards

**Models**
- [minilm-bo](https://github.com/billingsmoore/minilm-bo) — a Tibetan sentence-embedding model
  (superseded by `khyentsevision/minilm-bo-en-sim` for similarity tasks)
- [buddhist-domain-tagging](https://github.com/billingsmoore/buddhist-domain-tagging) — BERT
  classifiers tagging translations by subject domain

**Exploratory R&D**
- [exploratory-tibetan-asr](https://github.com/billingsmoore/exploratory-tibetan-asr) — Tibetan
  automatic speech recognition experiments
- [exploratory-tibetan-tts](https://github.com/billingsmoore/exploratory-tibetan-tts) — early
  Tibetan text-to-speech proof-of-concept work

**Writing**
- [openpecha-forum-posts](https://github.com/billingsmoore/openpecha-forum-posts) — published
  research write-ups on data cleaning, topic modeling, and knowledge graphs
