# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

MLotsawa is a Literary Tibetan → English (and to a lesser extent French/German/Spanish) machine
translation project, aimed at assisting (not replacing) human translators of Tibetan Buddhist texts.
It targets ordinary consumer laptops (8GB RAM, no GPU), not GPU servers.

The repo is a research monorepo, not a single application: it contains a large body of Jupyter
notebooks documenting dataset creation / model training / experiments, written research reports, and
an evaluation study. Most of the repo is historical research artifact, not live code — read dates
and folder names carefully before assuming something is current.

**Deprecated and removed**: the `PyPI/` package (the `mlotsawa` pip module + Flask WebUI),
`WordpressReact/` (docker-compose WordPress/React embed), and `ReactComponent/` (the standalone React
widget) have all been removed from this repo. They still exist in git history if needed for
reference, but there is currently no shipped end-user product in this repo — treat any surviving
references to them (docs, old commits) as historical.

**Also removed**: `EvalStudy/` (the human evaluation study — eval data, docx packets, and the
notebooks that generated them) has been removed. It was superseded by the actively developed
`human-eval-data-study` project in the separate KVP repo, which carried this same original data
forward (kept under `original-data-prep/` there) and continued the analysis with its own docs,
scripts, and figures.

`Docs/GarchenReport.{md,pdf}`, `Docs/res.png`, and `Notebooks/Experiments/ASR/XLSR/garchen/` (Garchen
Rinpoche-specific STT finetuning results, out of scope for this Tibetan→English translation project)
have also been removed — that work belongs to, and is already more fully documented in, the separate
Garchen repo (`R&D/ASR/Tibetan/Experiments/GeneralMaterialExperiment10-13/`).

`Docs/OpenPechaForumPosts/` (published research write-ups on data cleaning, topic modeling, and
knowledge graphs) has also been removed — it's a body of published writing, not translation-project
code, and now lives in its own repo: `~/Desktop/openpecha-forum-posts`
(https://github.com/billingsmoore/openpecha-forum-posts).

**All dataset creation/curation/formatting work has been split out**, since it's a distinct concern
from model training and translation-product code:
- `Notebooks/Datasets/B-MOP/` and `Docs/Datasets/B-MOP/` (BDRC-curated Tibetan OCR dataset-building
  notebooks and dataset cards — Betsug, Drutsa, KhyentseWangpo, LhasaKanjur, Google Books — pushed to
  `openpecha/`/`BDRC/` on the Hugging Face Hub) now live in `~/Desktop/bdrc-ocr-datasets`
  (https://github.com/billingsmoore/bdrc-ocr-datasets).
- The rest of `Notebooks/Datasets/` and `Docs/Datasets/` (84000, Aggregated, GNOME, Hopkins,
  LotsawaHouse, MadLad, Montano, NLLB, OpenPecha, stt-w-mt, Tatoeba, TED2020 — the translation-pair
  dataset creation/cleaning/formatting notebooks and the `AggregatedData.md` write-up) now live in
  `~/Desktop/tibetan-translation-datasets` (https://github.com/billingsmoore/tibetan-translation-datasets).
  Resulting datasets are published to the Hugging Face Hub and consumed from there by the model
  training notebooks that remain in this repo.

`Notebooks/Models/EmbeddingModel/` and `Docs/Models/MiniLM-BO.md` (training and clustering notebooks
for `billingsmoore/minilm-bo`, a Tibetan sentence-embedding model) have also been removed — this work
was continued downstream (the model was further finetuned into a sentence-similarity model used as an
automated translation quality metric in a separate project), so it now lives in its own repo:
`~/Desktop/minilm-bo` (https://github.com/billingsmoore/minilm-bo).

**All ASR (speech recognition) exploratory work has been removed**: `Notebooks/ExploratoryExperiments/ASR/`
(`ASRDialectLoRA/`, `ASRProofOfConcept/`, `Pretraining/`, `XLSR/`), `Notebooks/Experiments/ASR/KenLM/`,
and `Docs/WIP/ASRDialectLoRA.md` — Whisper proof-of-concept, dialect LoRA adaptation, wav2vec2
pretraining, and KenLM decoding language models. This is unrelated to the Tibetan→English translation
focus of this repo, so it now lives in its own repo: `~/Desktop/exploratory-tibetan-asr`
(https://github.com/billingsmoore/exploratory-tibetan-asr). Note there is also a separate, unrelated-
to-this-repo `asr-benchmarks` repo (private) holding a formal paper-scale ASR architecture benchmark —
`exploratory-tibetan-asr` is earlier/broader exploratory work, not that study.

## Repo layout

- `Notebooks/` — model training/experiment work, organized as `Models/<task>/<model>/...ipynb` and
  `Experiments/<topic>/...ipynb`. `ExploratoryExperiments/` holds one-off/abandoned experiments,
  separate from `Experiments/` (the more formal ablation work) and `Models/` (final training runs).
  Dataset creation notebooks now live in the separate `tibetan-translation-datasets`/
  `bdrc-ocr-datasets` repos (see above) — model notebooks here consume the resulting datasets from
  the Hugging Face Hub rather than building them locally.
- `Docs/` — written docs: `Models/`, `Experiments/` (formal write-ups mirroring Notebooks), `WIP/`
  (in-progress notes).
- `.venv/` — a local virtualenv; not part of the project, ignore/do not edit.

## Commands

### Notebooks

Notebooks assume a Jupyter environment with GPU-oriented ML libraries (transformers, torch, datasets,
etc.) and typically read/write from Hugging Face Hub (`billingsmoore/...` repos) — they are not
meant to be run without network access and HF credentials.

## Working conventions

- Model names referenced in notebooks/docs (e.g. `billingsmoore/mlotsawa-ground-small`,
  `billingsmoore/tibetan-phonetic-transliteration`) are live Hugging Face Hub repos; treat them as
  external dependencies, not something to modify in this repo.
- `Docs/ExplanationOfFolders.md` is currently just a one-line note about `Notebooks/Experiments/PreGround`; don't rely on it for a full folder explanation — this CLAUDE.md is more current.
