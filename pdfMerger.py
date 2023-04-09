"""
    Place File In Same Folder As All The PDFs.
    RECOMMENDED TO DELETE FILES MANUALLY INSTEAD OF USING THE SCRIPT!
"""

import os
import PyPDF2
import re
import subprocess


# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change the current working directory to the script directory
os.chdir(script_dir)

# Get all the PDF filenames
mainFiles = [file for file in os.listdir('.') if (file.endswith("pptx") or file.endswith("ppt") or file.endswith("docx") or file.endswith("doc")) and not re.match(fr'^(\d+)_(.+?)_Merged.pdf$', file)]

# Sort based on modification date
mainFiles.sort(key = lambda t: os.stat(t).st_mtime)    

print(mainFiles)

completed = 0
subject_name = os.getcwd().split('/')[-2]

# checks if previously merged file exists
for file in os.listdir('.'):
    match = re.match(fr'^(\d+)_(.+?)_Merged.pdf$', file)
    if match:
        completed = int(match.group(1))
        if completed > len(mainFiles):
            completed = 0
            os.remove(match.string)
        subject_name = match.group(2)
        break
print(f"Completed = {completed}")

# converts files to PDF and returns converted file list
convertedFiles = []
if len(mainFiles) > completed:
    for file in mainFiles[completed::]:
        # Get the file extension and base filename
        filename = os.path.splitext(file)[0]

        # Get the output PDF filename
        pdfFileName = filename + ".pdf"

        print(f"    Starting {pdfFileName}")

        # Convert the file to a PDF
        try:
            subprocess.call(['libreoffice', '--headless', '--convert-to', 'pdf', file])
        except subprocess.CalledProcessError:
            print(f"Unable to convert {pdfFileName}. Skipping...")    

        os.rename(pdfFileName, os.path.join(os.getcwd(), pdfFileName))
        convertedFiles.append(pdfFileName)
        print(f"    Completed {pdfFileName}!")

# lists all pdf files and sorts it
pdfFiles = [file for file in os.listdir(".") if file.endswith("pdf") and not re.match(fr'^(\d+)_(.+?)_Merged.pdf$', file)]
pdfFiles.sort(key = lambda t: os.stat(t).st_mtime)
print(f"PDF Files Are: {pdfFiles}")

merger = PyPDF2.PdfWriter()

# appends already created merged file
if completed > 0:
    merger.append(match.string)
    print(f"Merging Prevous {match.string}")
    os.remove(match.string)

# appends new files
for file in convertedFiles:
    merger.append(file)
    print(f"Merging {file}")
    completed += 1

# if merger is not empty
if merger:
    print(f"Writing Final PDF: {completed}_{subject_name}_Merged.pdf")
    # Name the merged document
    merger.write(f"{completed}_{subject_name}_Merged.pdf")
    merger.close()

print(f"Converted Files Are: {convertedFiles}")

# Delete ONLY those pdf files that were created with the script
for file in convertedFiles:
    os.remove(file)