"""
    Place File In Same Folder As All The PDFs.
    RECOMMENDED TO DELETE FILES MANUALLY INSTEAD OF USING THE SCRIPT!
"""

import os
import PyPDF2

choice = input("Would You Like To Delete Files After Merging? (y/n): ")

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change the current working directory to the script directory
os.chdir(script_dir)


# Get all the PDF filenames
pdfFiles = [filename for filename in os.listdir('.') if filename.endswith('.pdf')]

# Sort based on modification date
pdfFiles.sort(key = lambda t: os.stat(t).st_mtime)

merger = PyPDF2.PdfWriter()

# Append files
for file in pdfFiles:
    merger.append(file)

# Name the merged document
merger.write(f"{os.getcwd().split('/')[-1]}_Merged_PDF")
merger.close()

# Delete files
if choice.lower() == 'y':
    for file in pdfFiles:
        os.remove(file)