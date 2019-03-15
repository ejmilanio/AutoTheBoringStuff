###Lists Chapter 3

#list values refer to the list themselves. As in they are the value assigned to the variable
#items refer to data contained within a list. Seperated with commas.

spam = [[1,2,3], [4,5,6]]

spam[0][0]

###Negative indexes
#negative indexes searches lists starting from the end

spam = [1,2,3]
spam[-1]

###Getting sublists with slices
spam = [1,2,3,4,5]
spam[0:3]

### List concatenation and replication
spam = [1,2,3]
bacon = [1,2,3]
spam + bacon
spam * 3

###removing items with del
#only works at an index
spam = ['cat', 'dog', 'chicken', 'mouse']
del spam[1] # will remove dog
del 'chicken' #won't work
spam

###Working with lists
#avoids creating multiple variables for similar objects
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] #list concatenation
    print('The cat names are:')
    for name in catNames:
        print(' ' + name)

 
###Using For Loops with lists
for i in range(4):
    print(i)

#common tech for list manipulation is range(len(some_list)) with a for loop to iterate over the indexes of a list
supplies = ['pens', 'stapler', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i]) #gives BOTH index and name for each item in supplies

###The in and not in operators
#in statement will return a false or true statment depending whether item is found within list
#not in statment will return false or true statment depending whether item is NOT found with list
'howdy' in ['hello', 'hi', 'howdy', 'heyas']
spam = ['hello', 'hi', 'howdy', 'heyas']
'cat' in spam
'howdy' not in spam
'cat' not in spam

###The multiple assignment trick
#a shortcut that lets you assign multiple variables w/ values in a list
#long version
cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
print(size, color, disposition)

#short version
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
print(size, color, disposition)

#length of list must have exact number of matching variables

#can be used to swap the values in two variables
a, b = 'Alice', 'Bob'
print('a = ' + a)
print('b = ' + b)
a, b = b, a
print('a = ' + a)
print('b = ' + b)

###Methods
#Methods are the same as functions except they are "called on" a value
#ex. spam = value, index() = method
spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello')
spam.index('hi')
spam.index('howdy')
spam.index('heyas')

###Sorting with sort() method
#sort() sorts from least to greatest
spam = [2, 5, 3.14, 1, -7]
spam.sort()
spam
#sort sorts by ASCIIbetical order
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephents']
spam.sort()
spam

#sort() sorts the list in place. There is no return value
    #spam = spam.sort() does not work
#sort() doesn't sort lists with mix of int or str
#ASCIIbetical order. UPPERCASE comes before lowercase
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
spam

#use str.lower() for the key statement to sort in normal order
spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
spam

###Mutable and Immutable data types
#mutable -- CAN be changed, removed, or have values adjust
#immutable -- CANNOT be changed

#to mutate a string use slicing and concatenation
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
newName

###The Tuple data type
#like lists hey hold multiple values and can be accessed as such
eggs = ('hello', 42, 0.5)
eggs[0]
eggs[1:3]
len(eggs)
#like strings as they immutable
eggs = ('hello', 42, 0.5)
eggs[1] = 99

#if tuple has single value, follow that value with a comma
eggs = (99,)
type(eggs) #tuple
eggs = (99)
type(eggs) #int

###converting data type with tuple() and list()
#list() will turn an array into a list
list((1,2,3,))
#tuple() will turn an array in to a tuple
tuple([1,2,3])

###references
spam = 42
cheese = spam
spam = 100
spam #returns 100
cheese #returns 42
#spam and cheese return different values because they are different variables

#lists work differently. when assigning list to var you assign it a list REFERENCE.
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
spam
cheese

#in other words variables only hold the reference to a list

#Passing References
#when function is called values are passed to parameters
    #when a list used as a value only a COPY of the list is used

def eggs(someParameter):
    someParameter.append('Hello!')    

spam = [1, 2, 3]
eggs(spam)
print(spam)
 
#when eggs is called a there is no return statment
    #the function mutates spam in place and doesn't return a new list


### The copy module's copy() and deepcopy()
#allows to create a copy of a list and not just a copy of its reference

import copy 
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
spam
cheese

#how to work around variable sharing the same reference
#deepcopy() works for lists that contain other lists


