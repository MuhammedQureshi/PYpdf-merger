import PyPDF2
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilenames

# Select PDF files to merge using a file dialog
Tk().withdraw()
file_paths = askopenfilenames(filetypes=[("PDF Files", "*.pdf")])

# Create a PdfMerger object
merger = PyPDF2.PdfMerger()

# Iterate over selected files and append them to the merger
for file_path in file_paths:
    merger.append(file_path)

# Merge the files and save as "combined.pdf"
output_path = "combined.pdf"
merger.write(output_path)
merger.close()

print(f"Files merged successfully. Output saved as {output_path}.")
