import os

# Input and output file names
document = 'document.pdf'
output = 'output.pdf'

# Quality settings
small = 'screen'
medium = 'ebook'
print = 'printer'

'''
This program requires Ghostscript to be installed.
Compress the document with different options (/screen, /ebook, /printer) for quality of compression.

Example:
convertFile('file_to_compress.pdf', 'compressed_file.pdf', quality=(small, medium, or printer))
'''

def convertFile(document, output, quality):
    os.system(f'gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/{quality} -dNOPAUSE -dBATCH -sOutputFile={output} {document}')
    print("Document successfully converted")

# Example usage
convertFile('module_guide.pdf', 'output_1.pdf', small)
