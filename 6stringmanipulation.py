###Manipulating Strings

###Escape characters
#\' single quote
#\" double quote
#\t tab
#\n newline(line break)
#\\

###Raw Strings
#usefule for times where you type a lot of backslashes(\). Example would be Regex
#r'text'

###Indexing and slicing strings
"""
' H e l l o   W o r l d'
  0 1 2 3 4 5 6 7 8 9 10
"""

#Can slice strings like lists
spam = 'Hello world!'
spam[0]
spam[4] 
spam[-1]
spam[0:5] 
spam[:5]
spam[:6] 

#slicing doesn't modify original string. You can capture slice from one var to another
spam = 'Hello World'
fizz = spam[4:]
fizz

###The in and not in Operators with Strings
#in returns true if value is found in strings
#not in returns true if value is NOT found in string
'Hello' in 'Hello World!'
'Hello' in 'Hello'
'HELLO' in 'Hello World'
'' in 'spam'
'cats' not in 'cats and dogs'

###Useful string methods
#upper() turns string into all UPPERCASE
#lower() turns string into all lowercase

#upper() and lower() are usefule to check user inputs since most things are case sensitive
print('How are you?')
feeling = input()
if feeling.lower() == 'great': #GREAT, Great, GrEaT etc etc will all result in this executing
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')

#isupper() will check if there is at least one character and ALL characters are UPPERCASE
#islower() will check if there is at least one character and ALL characters are lowercase
spam = 'Hello world!'
spam.islower()
spam.isupper()
spam.upper().isupper()
'HELLO'.isupper()
'abc12345'.islower()
'12345'.islower()
'12345'.isupper()

### The isX string methods
#isalpha() will check if string is comprised of only letters and is not blank
#isalnum() will check if string is comprised of letters AND numbers
#isdecimal() will check if string is comprised of numbers and is not blank
#isspace() will check if string is comprised of spaces, tabs, and new-lines. Also will check if not blank.
#istitle() will check if string is in Title Case
'hello'.isalpha()
'hello123'.isalpha()
'hello123'.isalnum()
'hello'.isalnum()
'123'.isdecimal()
'       '.isspace()
'This Is Title Case'.istitle()

#also useful for confirming user inputs
while True:
    print('What is your age?')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age')

while True:
    print('Select a new password (letters and numbers only).')
    new_password = input()
    if new_password.isalnum():
        break
    print('Make sure password is only letters and numbers only.')

###The startswith() and endswith() string methods
#startswith() and endswith() checks if string value ends with given values
'Hello world!'.startswith('Hello')
'Hello world!'.endeswith('World!')
'abc123'.startswith('abcdef')
'abc123'.endswith('12')
'Hello world!'.startswith('Hello world!')
'Hello world!'.endswith('Hello world!')

#good alt to == because only checks for partial matches rather than entire matches

###The join() and split() string methods
#join() will combine a list of strings into one string
#split() will split a string into a list of strings
' '.join(['cats', 'dogs', 'birds', 'fish'])
', '.join(['cats', 'dogs', 'birds', 'fish'])
'aaa'.join(['cats', 'dogs', 'birds', 'fish'])

'Hello what is good?'.split()
'Hello what is good?'.split('!!!') #no triple exclamations to split at
'Hello what is good?'.split('o')

#useful to split multi line strings into multiple lists
spam = '''Dear Alice,
How have you been? I am Fine.
There is a container in the fridge
that is labled "Milk Experiment".

Please do not drink it.
Love,
Bob'''
spam.split('\n')

###Justifying text with with rjust(), ljust(), and center()
#rjust() will move text to the right x spaces
'Hello'.rjust(10)
#ljust() will move the text to the left x spaces
'Hello'.ljust(10)
#can place characters after first parameter and will fill with that chraracter instead of blank spaces
'Hello.'.rjust(10, '*')

#center() will just move text to the middle
'Hello'.center(20, '=')

#useful for creating tables to display data in which spacing would make it easeier to read
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') +str(v).rjust(rightWidth))
picnicItems = {'sandwhiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

###Removing whitespace with strip(), rstrip() and lstrip()
#removes whitespace from the string at the beginning and/or end
spam = '         Hello World           '
spam.strip()
spam.lstrip()
spam.rstrip()

#can enter values to be stripped at the end also
spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS')

###Copying and pasting strings with the pyperclilp module
import pyperclip
pyperclip.copy('Hello World!')
pyperclip.paste()
