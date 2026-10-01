# Create_BUSCO_Output_Excel.py

## Function

Recursively reads BUSCO text summaries and extracts completeness scores, assembly statistics, prediction mode and selected dependency versions.

## Overview

Collect genome completeness summaries into one Excel workbook.

## Context and contribution

I wrote this script for my final-year master’s research project investigating carbon-concentrating mechanisms in marine green algae.

Developed with assistance from ChatGPT. I defined the requirements, adapted and tested the code, checked outputs for errors, and debugged issues.

## How to use

Install pandas, tqdm and openpyxl. Set folder_path to the BUSCO summary folder and output_excel to an .xlsx filename. Run `python Create_BUSCO_Output_Excel.py`. The reader uses regular expressions matching the summary format used in the project.

Folder paths are placeholders: Input_BUSCO_Summaries. Replace them with your own locations before running. Relative paths are resolved from the working directory.
