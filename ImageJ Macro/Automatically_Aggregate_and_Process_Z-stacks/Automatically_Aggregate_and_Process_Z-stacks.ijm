refList = newArray(
    "1,Grey",
    "2,Grey",
    "3,Grey,Red",
    "4,",
    "5,Grey,Red",
    "6,Grey,Red",
    "7,Grey,Green,Blue,Red",
    "8,Grey,Green,Red",
    "9,Grey,Green,Red",
    "10,Grey,Green,Red",
    "11,Grey,Green,Red",
    "12,Grey,Blue,Red",
    "13,Grey,Blue,Red",
    "14,Grey,Blue,Red",
    "15,Grey,Green,Blue,Red",
    "16,Grey,Green,Blue,Red",
    "17,",
    "18,",
    "19,",
    "20,"
);

colourPriority = newArray("Grey", "Green", "Blue", "Red");

dir = getDirectory("Choose folder with ND2 files");
if (dir == "") exit("No folder selected");

list = getFileList(dir);

for (i = 0; i < list.length; i++) {

    if (endsWith(list[i], ".nd2")) {

        fileName = list[i];
        fullPath = dir + fileName;

        fileNumber = replace(fileName, "Slide", "");
        fileNumber = replace(fileNumber, ".nd2", "");

        parts      = split(fileNumber, "_");
        mainNumber = parts[0];
        subNumber  = "";
        if (parts.length > 1) {
            subNumber = "_" + parts[1];
        }

        slideColours = newArray(0);

        for (j = 0; j < refList.length; j++) {
            row = split(refList[j], ",");
            if (mainNumber == row[0]) {

                for (p = 0; p < colourPriority.length; p++) {
                    for (r = 1; r < row.length; r++) {
                        if (row[r] == colourPriority[p]) {
                            slideColours = Array.concat(slideColours, colourPriority[p]);
                        }
                    }
                }
                break;
            }
        }

        if (slideColours.length == 0) {
            continue;
        }

        run("Bio-Formats", "open=" + fullPath + " autoscale color_mode=Default rois_import=[ROI manager] split_channels view=Hyperstack stack_order=XYCZT");

        titles = getList("image.titles");
        for (t = 0; t < titles.length; t++) {
            if (startsWith(titles[t], fileName)) {
                selectImage(titles[t]);
                rename(replace(titles[t], " (33.3%)", ""));
            }
        }

        for (c = 0; c < slideColours.length; c++) {
            rawName    = fileName + " - C=" + c;
            colourName = fileName + " - C=" + c + " (" + slideColours[c] + ")";
            selectImage(rawName);
            rename(colourName);
        }

        savedFiles = newArray("", "", "", "");

        for (c = 0; c < slideColours.length; c++) {
            colour  = slideColours[c];
            winName = fileName + " - C=" + c + " (" + colour + ")";
            selectImage(winName);
            resetMinAndMax();
            run("Apply LUT", "stack");

            if (colour == "Grey") {
                run("Z Project...", "projection=[Max Intensity]");
                outFile = "MAX_" + fileNumber + " - C=" + c + " (Grey).png";
                saveAs("PNG", dir + outFile);
                savedFiles[0] = outFile;

            } else if (colour == "Green") {
                run("Z Project...", "projection=[Average Intensity]");
                outFile = "AVG_" + fileNumber + " - C=" + c + " (Green).png";
                saveAs("PNG", dir + outFile);
                savedFiles[1] = outFile;

            } else if (colour == "Blue") {
                run("Z Project...", "projection=[Max Intensity]");
                outFile = "MAX_" + fileNumber + " - C=" + c + " (Blue).png";
                saveAs("PNG", dir + outFile);
                savedFiles[2] = outFile;

            } else if (colour == "Red") {
                run("Z Project...", "projection=[Max Intensity]");
                outFile = "MAX_" + fileNumber + " - C=" + c + " (Red).png";
                saveAs("PNG", dir + outFile);
                savedFiles[3] = outFile;
            }
        }

        if (slideColours.length >= 2) {

            mergeCmd      = "";
            compositeName = "Composite";

            if (savedFiles[3] != "") {
                mergeCmd      = mergeCmd + "c1=[" + savedFiles[3] + "] ";
                compositeName = compositeName + "_Red";
            }
            if (savedFiles[1] != "") {
                mergeCmd      = mergeCmd + "c2=[" + savedFiles[1] + "] ";
                compositeName = compositeName + "_Green";
            }
            if (savedFiles[2] != "") {
                mergeCmd      = mergeCmd + "c3=[" + savedFiles[2] + "] ";
                compositeName = compositeName + "_Blue";
            }
            if (savedFiles[0] != "") {
                mergeCmd      = mergeCmd + "c4=[" + savedFiles[0] + "] ";
                compositeName = compositeName + "_Grey";
            }

            mergeCmd = mergeCmd + "create keep";
            run("Merge Channels...", mergeCmd);
            saveAs("PNG", dir + compositeName + "_" + fileNumber + ".png");
            close();
        }

        titles = getList("image.titles");
        for (k = 0; k < titles.length; k++) {
            selectImage(titles[k]);
            close();
        }
    }
}
