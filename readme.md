# PDF and Document Merger
This Python program is used to merge all **\`.pdf\`**, **\`.docx\`**, **\`.doc\`**, **\`.pptx\`**, and **\`.ppt\`** files in a directory into one merged **\`.pdf\`** file. The merged file is ordered based on the last modified (Oldest To Newest) date of the individual files.

## Prerequisites
To run this program, you will need:
- Python 3.6 or later
- PyPDF2 library
- LibreOffice (required to convert **\`.docx\`**, **\`.doc\`**, **\`.pptx\`**, and **\`.ppt\`** files to **\`.pdf\`**)

## How to Use
1. Place the Python file in the directory containing the files you want to merge.
2. Open the terminal or command prompt and navigate to the directory containing the Python file.
3. Run the command `python3 pdfMerger.py` to execute the program.

The merged .pdf file will be saved in the same directory as the original files. The merged file will be named according to the pattern:
`{Number of Completed Merges - 1}_{Name of Grand-Parent Directory Containing the Files}_Merged.pdf
`