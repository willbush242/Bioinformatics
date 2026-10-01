# ImageJ microscopy macro

## Function

Automate the processing of multi-channel Nikon ND2 microscopy images, split channels, generate Z projections and save individual-channel PNGs and merged composites.

## Overview

An ImageJ Macro Language (.ijm) tool for use in Fiji. It processes images using configurable slide-batch and channel assignments, reducing repeated manual steps across microscopy files.

## Contents

Automatically_Aggregate_and_Process_Z-stacks - A Fiji/ImageJ macro that automates the processing of multi-channel Nikon ND2 microscopy images. It uses a configurable list of slide batches and their channels to split image stacks, apply channel-specific Z projections and save individual-channel PNGs and merged composites.

## Context and contribution

I developed this macro during my final-year master's research into carbon-concentrating mechanisms in marine green algae. It supported the processing of immunofluorescence microscopy images.

Developed with assistance from ChatGPT. I defined the requirements, adapted and tested the code, checked outputs for errors, and debugged issues.

## How to use

Use Fiji with Bio-Formats available. Open the macro folder and follow its README to configure filenames, refList, channel order and projection settings. Check a representative image before processing a complete folder. Save and close unrelated images first because the macro closes all image windows during cleanup. Output PNGs are saved in the selected input folder.
