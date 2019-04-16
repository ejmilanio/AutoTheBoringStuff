###Organizing Files CH 9###

###The shutil Module
#The shells utility mod (shutil) lets you move, copy, rename and del files
import shutil

###Copying files and folders
#shutil.copy(source, destination)
    #parameters are "strings"
    #if destination is a filename, it will save as that filename
    #returns string of path of copied file
import shutil, os
os.chdir('C:\\')
shutil.copy('C:\\spam.txt', 'C:\\delicious')
shutil.copy('eggs.txt', 'C:\\delicious\\\eggs2.txt')

#shutil.copytree() will copy entire folder and all its contents
import shutil, os
os.chdir('C:\\')
shutil.copytree('C:\\bacon', 'C:\\bacon_backup')

###Moving and renaming folders
#shutil.move(source, destination)
import shutil
shutil.move('C:\\bacon.txt', 'C:\\eggs') #moves bacon.txt into eggs folder

#will overwrite any file that already has the name bacon.txt
#add new file name to end of destination to change the name
shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')

#if destination is a folder in root but not found will just rename the file
#assumes if no folder found then the file is just being changed to the "file name"
#if its a deeper folder and its not found then it will throw an error

###Permanently Deleting Files and Folders
#os.unlick(path) will delete the file at path
#os.rmdir(path) will delete the folder at path. Folder must be empty of files and folders
#shutil.rmtree(path) will remove the folder at path and all its contents
#***** test programs with by using a print() call at where they should be to see if they excecute at the right spot*****#
import os
for filename in os.listdir():  #os.listdir() gives filenames on the way to the path parameter in ()
    if filename.endswith('.rxt'):
        #os.unlink(filename)
        print(filename)

###Safe Deletes with send2trash module
import send2trash, os
baconFile = open('bacon.txt', 'a') #creates the file
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash('bacon.txt')

#send2trash.send2trash() sends to recycle bin
#doesn't free up hardrive space tho

###Walking a Directory Tree
import os
for folderName, subfolders, filenames in os.walk('C:\\delicious'): #passed a string the path of a folder
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)

#can us os.walk() much like range() where you can go through a loop of a set
#returns 3 values on each iteration of a loop
    #1 A string of the current folder's name
    #2 A list of strings of the folder in the current folder
    #3 A list of strings of the files in the current fodler

#if sub folders or filenames aren't need to be looped to just remove the for statement for that parameter

###Compressing files with the zipfile module 
#ZipFile objects == to File objects
import zipfile, os
os.chdir('C:\\')
exampleZip = zipfile.ZipFile('example.zip') #works like open()
exampleZip.namelist()                       #namelist() returns list string of files/folders in zip file (hint: LOOP THROUGH IT)
spamInfo = exampleZip.getinfo('spam.txt')   #pass name list to getinfo()
spamInfo.file_size                          #returns original size of a file
spamInfo.compress_size                      #returns compressed size of file
'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2))
exampleZip.close()

#getinfo() is a method from ZipFile module and returns an object called ZipInfo
    #.file_size and .commpress_size are attributes of the method getinfo()

#ZipFile == entire zip file
#zipinfo == single file within zipped folder

###Extracting from ZIP files
#extractall() extracts all files/folders into current working directory
import zipfile, os
os.chidir('C:\\')
exampleZip = zipfile.ZipFile('example.zip')     #opens targeted zipfile
exampleZip = exctractall()                      #can place a designated location in parameters. if file doesn't exist will create a file at location
exampleZip.close()

#extract() will extract a single file
exampleZip.extract('spam.txt')
exampleZip.extract('spam.txt', 'C:\\some\\new\\folder') #will extract to a designated folder
exampleZip.close()

###Creating and Adding to ZIP files
#must open ZipFile object in write mode by passing 'w' as second parameter
    #much like open('text.txt', 'w')
#write() method will compress the file
    #first paramter is string of the filename to add
    #second parameter is compression type
        #put which algorithm to use to compress
            #done by setting value to zipfile.ZIP_DEFLATED.
import zipfile
newZip = zipfile.ZipFile('new.zip', 'w')                        #creates an editable zipfie
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)    #places the compressed content of 'spam.txt' into the zipfile
newZip.close()
.













0