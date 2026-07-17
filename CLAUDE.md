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

## Repo layout

- `Notebooks/` — all model/dataset development work, organized as `Datasets/<source>/...ipynb` and
  `Models/<task>/<model>/...ipynb`. `ExploratoryExperiments/` holds one-off/abandoned experiments,
  separate from `Experiments/` (the more formal ablation work) and `Models/` (final training runs).
- `Docs/` — written docs: `Datasets/`, `Models/`, `Experiments/` (formal write-ups mirroring
  Notebooks), `OpenPechaForumPosts/` (published research posts on data cleaning, topic modeling,
  knowledge graphs), `WIP/` (in-progress notes), plus `GarchenReport.{md,pdf}`.
- `EvalStudy/` — a human evaluation study: `Code/` (notebooks to build eval docx packets from data),
  `Data/` (csv/ods rating data), `84000/` and `KVP/` (generated `.docx` evaluation packets,
  reference and reference-free variants).
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
