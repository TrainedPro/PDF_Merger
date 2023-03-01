"""
    Place File In Same Folder As All The PDFs.
    RECOMMENDED TO DELETE FILES MANUALLY INSTEAD OF USING THE SCRIPT!
"""

import os
import PyPDF2
import re

choice = input("Would You Like To Source Delete Files After Merging? (y/n): ").lower() == 'y'

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change the current working directory to the script directory
os.chdir(script_dir)

# Get all the PDF filenames
pdfFiles = [file for file in os.listdir('.') if file.endswith('.pdf') and not re.match(r'^(\d+)_(.+?)_Merged.pdf$', file)]

# Sort based on modification date
pdfFiles.sort(key = lambda t: os.stat(t).st_mtime)

print(pdfFiles)

prev = 0
subject_name = os.getcwd().split('/')[-2]

for file in os.listdir('.'):
    # Check if the filename matches the regex pattern
    match = re.match(r'^(\d+)_(.+?)_Merged.pdf$', file)
    if match:
        prev = int(match.group(1))
        if prev > len(pdfFiles):
            prev = 0
            os.remove(match.string)
        subject_name = match.group(2)
        break
print(f"prev = {prev}")


merger = PyPDF2.PdfWriter()

if prev > 0:
    merger.append(match.string)
    print(f"Merging Prevous {match.string}")
    os.remove(match.string)


# Append files
for file in pdfFiles[prev::]:
    merger.append(file)
    print(f"Merging {file}")
    prev += 1

# Name the merged document
merger.write(f"{prev}_{subject_name}_Merged.pdf")
merger.close()


# Delete files
if choice:
    for file in pdfFiles:
        os.remove(file)