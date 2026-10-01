# Bash gene-prediction scripts

## Function

Run BRAKER gene prediction across folders of genome FASTA files and organise the results into separate working directories for each genome.

## Overview

Bash scripts for automating repeated BRAKER runs. The two scripts use different settings: one supplies reference proteins and reuses an AUGUSTUS species configuration, while the other runs in ES mode without parameter optimisation.

## Contents

Run_Braker_Skip_Optimise - Batch-run BRAKER in ES mode without parameter optimisation.

Run_BRAKER - Run BRAKER gene prediction across a folder of genome FASTA files.

## Context and contribution

I developed these scripts for my final-year master's research project investigating carbon-concentrating mechanisms in marine green algae.

Developed with assistance from ChatGPT. I defined the requirements, adapted and tested the code, checked outputs for errors, and debugged issues.

## How to use

Use Ubuntu on Windows Subsystem for Linux (WSL), with BRAKER and its dependencies configured. Follow the individual README to set genome, output and executable paths, and any reference-protein or species settings. Use Linux paths and run the selected script with bash. Both scripts are configured for eight threads; review resource settings for your system.
