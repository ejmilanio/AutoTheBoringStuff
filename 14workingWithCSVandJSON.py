###-------------------------------------------------------###
#       Ch 14. Working with CVS Files and JSON Data         #
###-------------------------------------------------------###

### Working w/ CVS and JSON ###
#Plain files, viewable in a text editor
#uses csv and json modules

#CSV stands for 'comma-seperated values'
    #simplified spreadsheets

#JSON stands for JavaScript Object Notation
    #stores info as JS source code in plaintext
    #JS isn't needed to know JSON but it's useful to know the module due to the prevalence of JS

### THe CSV Module ###
#CSV files are simple
    #Don't have types for their values -- everything is a string
    #Don't have settings for font size or color
    #Don't have multiple worksheets
    #Can't specify cell widths and heights
    #Can't have merged cells
    #Cant have imag or charts embedded in them

#Advantage is in its simplicity.
    #Widely supported
    #Viewable in simple text editors
    #Straight forward way to represent spreadsheet data
    
#Use csv mod to parse
    #split() and other parsing tools can't deal with the commas

### Reader Objects ###
#To read data from a CSV file create a Reader obj
import csv
exampleFile = open('example.csv')           
exampleReader = csv.reader(exampleFile)     #csv.reader() creates a Reader Obj
exampleData = list(exampleReader)
exampleData

#can access data by accessing value at a row/column
    #row == index of one of the lists in the csv file
    #col == index of item within the list called in the row
exampleData[0][0]
exampleData[0][1]
exampleData[0][2]
exampleData[1][1]
exampleData[6][1]

### Reading Data from Reader Obj in a for Loop ###
#useful for saving memory when accessing 
import csv
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
    print('There are ' + str(row[2]) + ' ' + str(row[1]))

for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row)) #each Reader obj can only be looped over once
                                                                  #Need to create a new Reader obj

### Writer Objects ###
import csv
outputFile = open('output.csv', 'w', newline = '')                      #Call open() to create a new file. Make sure its in 'w' or write mode. If newline argument is not called csv file will be double spaced
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'rice'])                #writerow() creates a new row. Takes a list as its arg
outputWriter.writerow(['Hello, world!', 'Goodbye cruel world', 'fml', 'im learning'])
outputWriter.writerow([3.14, 1, 2, 99])
outputFile.close()                                                      #don't forget to close the file

### The Delimiter and Lineterminator Keyword Arguments ###
import csv
csvFile = open('example.tsv', 'w', newline = '')
csvWriter = csv.writer(csvFile, delimiter= '\t', lineterminator= '\n\n')
csvWriter.writerow(['apples', 'oranges', 'grapes'])
csvWriter.writerow(['eggs', 'bacon', 'ham'])
csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
csvFile.close()