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

`Notebooks/Datasets/B-MOP/` and `Docs/Datasets/B-MOP/` (BDRC-curated Tibetan OCR dataset-building
notebooks and dataset cards — Betsug, Drutsa, KhyentseWangpo, LhasaKanjur, Google Books — pushed to
`openpecha/`/`BDRC/` on the Hugging Face Hub) have also been removed. This is OCR dataset curation
work, not translation, so it now lives in its own repo: `~/Desktop/bdrc-ocr-datasets`.

## Repo layout

- `Notebooks/` — all model/dataset development work, organized as `Datasets/<source>/...ipynb` and
  `Models/<task>/<model>/...ipynb`. `ExploratoryExperiments/` holds one-off/abandoned experiments,
  separate from `Experiments/` (the more formal ablation work) and `Models/` (final training runs).
- `Docs/` — written docs: `Datasets/`, `Models/`, `Experiments/` (formal write-ups mirroring
  Notebooks), `OpenPechaForumPosts/` (published research posts on data cleaning, topic modeling,
  knowledge graphs), `WIP/` (in-progress notes).
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
