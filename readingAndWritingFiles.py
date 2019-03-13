#Windows OS uses backslashes(\) as a seperator between file names
#OS X and Linux use forwardslashes(/) as seperators between file names
#os.path.join() will return string for all OS
import os
os.path.join('usr', 'bin', 'spam')

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('C:\\Users\\asweigart', filename))

# os.getcwd() will return the CURRENT WORKING DIRECTORY
import os
os.getcwd()

#XXX dont actually change the directory at this point
# os.chdir() will change the CWD to what is specified in the parameters of the function
    # os.chdir(C:\\User....etcetc)

### ABSOLUTE VS RELATIVE PATHS
#ABSOLUTE PATH always begins with root folder
#RELATIVE PATH depends on programs current working directory
    #dot(.) for a folder name is shorthand for "this directory"
    #dot-dot(..) for a folder name is shorthand for "parent directory"

#os.path.abspath(path) will return a string of the absolute path of the argument
    #useful for turning relative path to absolute
import os
os.path.abspath('.')
os.path.abspath('.\\Scripts')

#.isabs(path) will return True if arg is abs path and False if rel path
os.path.isabs('.')
os.path.isabs(os.path.abspath('.'))

#relpath(path, start) will return string of rel path from start to path.
    #if start is blank, defaults to CWD as start path
import os
os.path.relpath('C:\\Windows', 'C:\\')
os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')
os.getcwd()

#os.path.dirname(path) will return a string of everything BEFORE the last slash of the path argument
#os.path.basename(path) will return of string of everything AFTER the last slash of the path argument
import os
path = 'C:\\Windows\\System32\\calc.exe'
os.path.basename(path)
os.path.dirname(path)
    #dirname is """C:\\Windows\\System32\\calc.exe"""
    #basename is """calc.exe"""

#os.path.split() creates tuple of dirname and base name
import os
calcFilePath = 'C:\\Windows\\System32\\calc.exe'
os.path.split(calcFilePath)

#alternatively just place .dirname and .basename in a tuple
(os.path.dirname(calcFilePath), os.path.basename(calcFilePath))

#To return string of each folder name use split() on os.sep
calcFilePath.split(os.path.sep)
    #OS X and Linux will return a blank string at the start of list

###FINDING FILE SIZE AND FOLDER CONTENTS
#ospath.getsize(path) will return size in bytes of file in path arg
#os.listdir(path) will return list of filenames stings for each file in path arg
import os
os.path.getsize('C:\\Windows\\System32\\calc.exe')
os.listdir('C:\\Windows\\System32')

#using .getsize() and .listdir() will return size of all files in dir
totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
    totalSize += os.path.getsize(os.path.join('C:\\Windows\\System32', filename))

print(totalSize)

###CHECKING PATH VALIDTY
#os.path.exists(path) returns True if file/folder in arg exists
    #returns False if doesn't
#os.path.isfile(path) returns True if path arg exists AND is File
    #returns False if isn't
#os.path.isdir(path) will return True if path arg exists AND is a folder
    #returns False if isn't
import os
os.path.exists('C:\\Windows')
os.path.exists('C\\some_made_up_folder')
os.path.isdir('C:\\Windows\\System32')            #dir
os.path.isfile('C:\\Windows\\System32')           #dir
os.path.isdir('C:\\Windows\\System32\\calc.exe')  #file
os.path.isfile('C:\\Windows\\System32\\calc.exe') #file

###THE FILE READING/WRITING PROCESS
#Plaintext files just contain characters and no formatting 
    #include .txt files and .py files
    #can be opened in programs such as notepad
#Binary files are all other types such as .pdf, .word, spreadsheets etc
    #binary files if opened in notepad will look like a scrambled mess

#Three major steps
    #1) open() to return a file object
    #2) read() or write() method on a file object
    #3) close() method to close a file object

###OPENING FILES WITH open()
#pass in string with the open() function
    #takes abs or rel path
import os
helloFile = open('C:\\Users\\ejmil\\Documents\\helloworld.txt')

#adding 'r' at the end of parameters for open() you can specify what mode
#it opens in open('/Users/blah/blah.txt', 'r')

#open() calls a file object
#treat like another data type

###READING THE CONTENTS OF FILES
#read() reads file object
import os
helloFile = open('C:\\Users\\ejmil\\Documents\\helloworld.txt')
helloContent = helloFile.read()
helloContent

#readlines() method creates a list of strings.
    #one string per line
import os
sonnetFile = open('C:\\Users\\ejmil\\Documents\\sonnet29.txt')
sonnetFile.readlines()

###WRITING TO FILES
#cant write to opened files
    #must open in "write plaintext" or "append plaintext" mode
        #pass 'w' as second arg for open() for write mode. Overwrites existing file and starts from scratch.
        #pass 'a' as second arg for open() for append mode. Append text to the end of the text file.
    #calling write() on file will use passed text to write or append file
import os
baconFile = open('C:\\Users\\ejmil\\Documents\\bacon.txt', 'w')
baconFile.write('Hello world!\n')
baconFile.close()
baconFile = open('C:\\Users\ejmil\\Documents\\bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
baconFile = open('C:\\Users\\ejmil\\Documents\\bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)

#writes multiple files and adds 1 digit to the name. useful for repetitive files.
import os
testVar = 'testname'
testNameCount = 1
for i in range(0 ,3):
    testFile = open('C:\\Users\\ejmil\\Documents\\' + testVar + str(testNameCount), 'w') #replace test name count with i+1 from the for loop
    testFile.write('Hello world!\n')
    testFile.close()
    testNameCount += 1 #remove

###SAVING VARIABLES WITH THE SHELVE MODULE
#will let you add save and open features to the program
import shelve, os
shelfFile = shelve.open('C:\\Users\\ejmil\\Documents\\mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

#check if above code worked
import shelve, os   
shelfFile = shelve.open('C:\\Users\\ejmil\\Documents\\mydata')
type(shelfFile)
shelfFile['cats']
shelfFile.close()

#shelf values have keys() and values() like dictionaries
import shelve, os
shelfFile = shelve.open('C:\\Users\\ejmil\\Documents\\mydata')
list(shelfFile.keys())
list(shelfFile.values())
shelfFile.close()

###SAVING VARIABLES WITH THE PPRINT.PFORMAT() FUNCTION
import pprint, shelve, os   
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
fileObj = open('C:\\Users\\ejmil\\Documents\\myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) +'\n')
fileObj.close()
