# POS Tagger with Majority and Hidden Markov Model (HMM)

## Overview
This project implements two Part-of-Speech (POS) tagging models:
1. **Majority Tagger**: A simple approach that assigns the most common tag for each word based on training data.
2. **Hidden Markov Model (HMM) Tagger**: A more advanced model using a probabilistic approach with the Viterbi algorithm, designed to handle unseen words using heuristics.

Developed for **CSC 583: Algorithms for NLP**, these models demonstrate efficient POS tagging methods in Python.

## Features

- **Majority Tagger**:
  - Calculates and stores the most common tag for each word based on training data.
  - Tags unseen words as `NN` (noun) by default.

- **HMM Tagger**:
  - Calculates transition and emission probabilities using training sentences.
  - Uses add-one smoothing for unseen tag transitions.
  - Applies heuristic rules for tagging unseen words based on character patterns (e.g., `-ly` suggests `RB`, `-ing` suggests `VBG`).
  - Utilizes the Viterbi algorithm for optimal tag sequence prediction.

