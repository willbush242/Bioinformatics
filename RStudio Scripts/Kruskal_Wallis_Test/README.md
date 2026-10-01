# Kruskal_Wallis_Test.R

## Function

Reads Excel, removes rows missing Number or N_Rate, retains groups 1–7 and performs the rank-based test.

## Overview

Compare respiration measurements across experimental groups using a Kruskal–Wallis test.

## Context and contribution

I wrote this script for my third-year university research project investigating respiration in marine microorganisms.

Developed with assistance from ChatGPT. I defined the requirements, adapted and tested the code, checked outputs for errors, and debugged issues.

## How to use

Install readxl and dplyr. Set the Excel path and sheet in read_excel. Supply Number (group) and N_Rate (numeric measurement). Run in RStudio or `source("Kruskal_Wallis_Test.R", echo = TRUE)`.

Folder paths are placeholders: Input_Folder/Input_Data.xlsx. Replace them with your own locations before running. Relative paths are resolved from the working directory.
