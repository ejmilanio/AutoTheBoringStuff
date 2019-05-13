###---------------------------------------------------------------###
#       Ch 12 Project: Combining Select Pages from Many PDFS        #
###---------------------------------------------------------------###
"""
This project must...
    Find all the PDF files in the current working directory
    Sort the file names so the PDFS are added in order
    Write each page, exluding the first page of each PDF to the output file
        In terms of implementation, your code will need to to do the following...
            -Call os.listdir() to find all the files in the working directory and remove any non-PDF files
            -Call python's sort() list method to alphabetize the filenames
            -Create a PdfFileWriter obj for the output PDF
            -Loop over each PDF file, creating a PdfFileReader obj
            -Loop over each page (except the first) in each PDF file
            -Add the pages to the output PDF
            -Write the output PDF to a file named allminutes.pdf                             
"""
#! python3
import PyPDF2, os

#Find All PDFs
pdfFiles = []
for filenames in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key= str.lower)

pdfWrite = PyPDF2.PdfFileWriter()

# Open each PDF
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)


pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()

