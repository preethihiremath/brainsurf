# BrainSurf Sample Data

This folder contains EEG and Stroop samples used by the BrainSurf notebooks.

## Organization

- `cohort/adarsh/`
  - `eeg/`: pre-, during-, and post-meditation EEG.
  - `cognitive/`: pre/post cognitive-task EEG files.
  - `stroop/`: pre/post Stroop behavioural results.
  - `ml/`: labelled EEG files used by the machine-learning notebook cells.
- `cohort/anirudh/eeg/`: pre-, during-, and post-meditation EEG.
- `cohort/yogesh/eeg/`: pre- and post-meditation EEG.
- `mantra_meditation/`: externally supplied mantra-meditation spectral data. These files are intentionally left unchanged.
- `reference/`: generic demo/reference files, including EDF/XLSX samples and the local MFF reference directory.

## Session Labels

- `pre_meditation`: baseline EEG before meditation.
- `during_meditation`: EEG captured during meditation.
- `post_meditation`: EEG captured after meditation.
- `pre_cognitive` / `post_cognitive`: EEG captured around cognitive-task analysis.
- `pre_stroop` / `post_stroop`: Stroop behavioural results for reaction time and accuracy analysis.

Adarsh recordings already included `sec,EEG` columns. Anirudh and Yogesh EEG-only files were normalized to the same `sec,EEG` layout using an assumed 200 Hz sampling rate (`sec = row_index / 200`).

`sample_manifest.csv` lists each organized sample file, participant/source, session state, modality, columns, row count, and source notes.
