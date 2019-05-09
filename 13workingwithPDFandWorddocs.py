###---------------------------------------------###
#      Ch. 13 Working with PDF and Word Docs      #
###---------------------------------------------###

import os
os.chdir("C:\\Users\\ejmil\\source\\repos\\AutoTheBoringStuff")

### Extracting Text from PDF files ###
import PyPDF2 
pdfFileObj = open('meetingminutes.pdf', 'rb')           #open PDF file in 'read binary' mode; creates a PDFFile Object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)            #create a PdfFileReader object and pass it PDFFile obj

pdfReader.numPages                                      #attr of a PdfFileReader object
pageObj = pdfReader.getPage(0)                          #.getPage() takes a page. An arrray so starts from 0
pageObj.extractText()                                   #.extractText() function extracts text

### Decrypting PDFs ###
#some PDFs are encrypted and need passwords

import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
pdfReader.isEncrypted                                   #checks if encrypted; boolean value
pdfReader.decrypt('rosebud')                            #returns 1 if password is correct; 0 if password is incorrect
pdfReader.getPage(0)

### Creating PDFs ###
#Must create a PdfFileWriter object to create a PDF
#PyPDF2 can only copy pages from other PDFs, roatate pages, overlay pages and encrypt files

#PyPDF2 cant directly edit a PDF. Must create new PDF and copy content to the new PDF
    #1. Open one ore more existing PDFs (the source PDFs) into PdfFileReader objects
    #2. Create a new PdfFileWriter Object.
    #3. Copy pages from the PdfFileReader objects into the PdfFileWriter Object
    #4. Finally, use the PdfFileWriter object to write the output PDF.

#PdfFileWriter object only represents a PDF doc and doesn't actually create one
    #PdfFileWriter's write() method will create a PDF file

#@ Copying Pages @#

import PyPDF2
pdf1File = open('meetingminutes.pdf', 'rb')         #open both PDFs in 'read binary' mode
pdf2File = open('meetingminutes2.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)         #create a PdfFileReader object for both PDFs
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
pdfWriter = PyPDF2.PdfFileWriter()                  #create a PdfFileWriter for new combined PDF

for pageNum in range(pdf1Reader.numPages):          #loop through each page in the 1st PDF
    pageObj = pdf1Reader.getPage(pageNum)           #create a Page object for each page
    pdfWriter.addPage(pageObj)                      #append each Page object to the PdfFileWriter object

for pageNum in range(pdf2Reader.numPages):          #Loop through each page in the 2nd PDF and append to the PdfFileWriter
    pageObj = pdf2Reader.getPage(pageNum)           #create a Page object for each page
    pdfWriter.addPage(pageObj)                      #append each Page object to the PdfFileWriter object

pdfOutputFile = open('combinedminutes.pdf', 'wb')   #create a new PDF by passing a File obj to the PdfFileWriters write() method
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()

#@ Rotating Pages @#
#Pages can be rotated 90 degree increments with the rotateClockwise() and rotateCounterClockwise() methods
    #can be passed 90, 180 or 270 arguments 

import PyPDF2
minutesFile = open('meetingminutes.pdf', 'rb')          #open a PDF in 'read binary' mode
pdfReader = PyPDF2.PdfFileReader(minutesFile)           #create a PdfFileReader object
page = pdfReader.getPage(0)                             #create a Page object
page.rotateClockwise(90)                                #rotate that Page object clockwise 90 degrees
pdfWriter = PyPDF2.PdfFileWriter()                      #create a PdfFileWriter object
pdfWriter.addPage(page)                                 #append roated page to the object
resultPdfFile = open('rotatedPage.pdf', 'wb')           #open the PdfFileWriter object
pdfWriter.write(resultPdfFile)                          #save the PdfFilewriter object
resultPdfFile.close()                                   #close the new PdfFileWriter object
minutesFile.close()                                     #close original PdfFileWriter object










