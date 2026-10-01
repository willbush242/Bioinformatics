# Automatically_Aggregate_and_Process_Z-stacks.ijm

## Function

- Processes the .nd2 files directly inside a selected folder.
- Identifies the slide batch from each filename and looks up its channel list.
- Orders the channels according to the microscope's channel order rather than the order of colours written in the slide list.
- Imports ND2 files through Bio-Formats as split-channel hyperstacks using XYCZT stack order.
- Labels each imported channel window with its assigned colour.
- Resets the display range and applies the existing lookup table to each channel stack.
- Uses maximum-intensity Z projections for Grey, Blue and Red, and average-intensity Z projections for Green.
- Saves the projections as PNG files and, when two or more channels are configured, creates a merged composite.
- Closes image windows after each processed file before continuing to the next file.

## Overview

A Fiji/ImageJ macro that automates the processing of multi-channel Nikon ND2 microscopy images. It uses a configurable list of slide batches and their channels to split image stacks, apply channel-specific Z projections and save individual-channel PNGs and merged composites.

## Context and contribution

I developed this macro during my final-year master's research project investigating carbon-concentrating mechanisms in marine green algae. It supported the processing of immunofluorescence microscopy images.

Developed with assistance from ChatGPT. I defined the requirements, adapted and tested the code, checked outputs for errors, and debugged issues.

## How to use

### 1. Prepare Fiji

Use Fiji with Bio-Formats available. Open Automatically_Aggregate_and_Process_Z-stacks.ijm in Fiji's script editor and select the ImageJ Macro language if it is not selected automatically. The file is an ImageJ macro, not Python, despite the name of its parent folder.

Close unrelated image windows before running: the cleanup loop closes all image windows, not only those opened by this macro. Save any work in progress first. Work from a copy of the ND2 folder if you want to keep generated files separate from your original dataset.

### 2. Prepare the input filenames

Use names such as Slide1_3.nd2. In this example, 1 identifies the slide batch and 3 identifies an image within that batch. The part before the underscore is matched against refList. Multiple images from the same batch therefore share one channel configuration.

Use the exact Slide prefix and lowercase .nd2 extension expected by the code. Place the files directly in the selected folder: the macro does not search subfolders. The import command inserts the full path without brackets, so use a folder path without spaces for this version.

### 3. Configure refList

Each quoted row contains a slide-batch number followed by the channels present in that batch, separated by commas. For example:

    "1,Grey"
    "3,Grey,Red"
    "7,Grey,Green,Blue,Red"

Use exactly the supported colour labels Grey, Green, Blue and Red. These labels describe the channel/laser assignments in the experiment. Check them against the microscope acquisition settings; the macro does not infer a channel's biological identity from the image.

Add as many batch entries as needed. In the newArray declaration, put a comma after each row except the final row. A row such as "4," has no configured channels, so files for that batch are skipped. Files with no matching batch entry are also skipped.

Keep one row per batch number: the lookup stops at the first match. Slide 12 is configured once, with Grey, Blue and Red channels.

### 4. Check colourPriority against the microscope

The supplied order is:

    Grey, Green, Blue, Red

This determines which configured colour is assigned to C=0, C=1 and subsequent channel windows. Only colours present for that slide are retained. A Grey/Red slide therefore maps Grey to C=0 and Red to C=1; a four-channel slide maps Grey, Green, Blue and Red to C=0, C=1, C=2 and C=3 respectively.

To confirm the order, manually open a representative ND2 file through Bio-Formats with split channels and inspect the channel windows and acquisition information. C=0 is the first channel, C=1 the second, and so on. Edit colourPriority if the microscope uses a different order. Confirm that the number of listed colours matches the acquired channels.

The macro sorts each slide's colour list through colourPriority, so the order in which colours appear in a refList row is not used to assign channels. The original notes state that reordering refList colours had not been tested; verify the mapping on a representative file when changing the configuration.

### 5. Check the projection settings

The processing branches use the following settings:

    Colour   Z projection        savedFiles index   Merge Channels slot
    Grey     Maximum intensity   0                  c4
    Green    Average intensity   1                  c2
    Blue     Maximum intensity   2                  c3
    Red      Maximum intensity   3                  c1

These are the settings used in this project, not automatically selected settings for every experiment. Change the relevant Z Project command if your analysis requires a different projection. The macro resets the display range and applies the imported LUT before projecting; it does not explicitly set a separate LUT by colour name.

The merge slots assign Red to c1, Green to c2, Blue to c3 and Grey to c4. These are separate from the zero-based C= channel numbers assigned at import.

### 6. Run the macro

Save the configured macro and run it in Fiji. Choose the folder containing the ND2 files when prompted. Cancelling folder selection stops the macro.

For each matching file, the macro imports split channels, removes the literal " (33.3%)" suffix from matching image titles if present, then looks for channel windows named filename.nd2 - C=0 and so on. Check those titles in a manual import if Fiji cannot find a channel window.

The macro processes each configured channel, saves its projection and builds a merge command using only the saved channels. Composites are created when at least two channels are configured. A single-channel file receives an individual projection only.

### 7. Locate the saved files

All PNGs are saved in the selected input folder. Projection filenames contain MAX_ or AVG_, the slide/image identifier, the imported C= index and the colour label. Composite filenames begin Composite, include the processed colour names in Red/Green/Blue/Grey order, and end with the slide/image identifier.

The source ND2 files are opened but are not saved over by the macro. Existing PNGs with the generated names may be replaced or prompt for overwrite, depending on Fiji's save behaviour; use a fresh output working folder when rerunning with different settings.

## Adding more colours or channels

The original end-of-file instructions have been moved here and expanded into the following steps:

1. Add the new colour name to colourPriority in the correct acquisition order. Open a representative file with split channels first and inspect its C=0, C=1 and subsequent windows to determine that order.

2. Add the new colour to the relevant refList rows, keeping a single entry per slide batch. Do not add a trailing comma after the last array row.

3. Expand savedFiles to hold another channel. It currently contains four empty strings. For a fifth channel, use newArray("", "", "", "", ""). Keep the existing indices unchanged unless you also update every reference to them.

4. Add an else if branch to the channel-processing loop. Match the new colour label exactly, choose its projection method, build a distinct output filename, save the PNG and store the filename in the new savedFiles index.

5. Add the corresponding condition to the merge-command builder. Choose an appropriate additional slot supported by Fiji's Merge Channels command, add the saved filename to that slot and append the colour label to compositeName. The existing slots c1 through c4 are already assigned.

6. Check one representative file manually before running the complete folder, confirming channel identity, projection choice, output names and composite colours.
