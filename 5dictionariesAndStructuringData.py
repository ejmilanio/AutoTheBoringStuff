### Dictionaries and Structuring Data ###

###Dictionary Data Type
    #key is the 'index' for dictionaries
    #value is what is held by the key
    #often spoken of together as key-value pairs

#Dictionaries are often closed in {}

myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

#keys are size, color and disposition
#values are fat gray and loud

#You access values by calling the keys
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
myCat['size']
'My cat has ' + myCat['color'] + ' fur'

#possible to use numbers as keys. but doesn't neccisarily have to start at 0

###Dictionaries vs lists
#dictionaries aren't in an order // lists are ordered
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
spam == bacon #will return False

eggs = {'name': 'Zophie',
        'species': 'cat',
        'age': '8'}
ham = {'species': 'cat',
       'age': '8',
       'name': 'Zophie'}
eggs == ham #will return True

#dictionaries cannot be sliced since they have no order
#you can have arbitrary values for keys to organize data

birthdays = {'Alice': 'Apr 1',
             'Bob': 'Dec 12',
             'Carol': 'Mar 4'
             }

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    
    if name in birthdays:   
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthdays database updated.')

###The get() method
#takes two arguments; key and value
#searches for key. if not found looks for value
picnicItems = {'apples': 5, 'cups': 2,}
'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.' #since there is no egg key, 0 is returned as the default value

###The setdefault() Method
spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'

print(spam)

#setdefault 2 arg (key to be checked for, value to set if not found)
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
spam
spam.setdefault('color', 'white') #won't work because the key 'color' has been found since it was set in the previous lines
spam

message = 'It wascks  a bright cold day in APril, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1

print(count)

###Pretty Printing

import pprint
message = 'It wascks  a bright cold day in APril, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1

pprint.pprint(count)

###Nested dictionaries and lists
allGuests = {'Alice': {'apples:': 5, 'pretzels': 12},
             'Bob': {'ham sandwhiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}
             }

def totalBrought(guests, items):
    numBrought = 0
    for k, v in guests.items():
        numBrought += v.get(items,0)
    return numBrought

print('Nprint(' -Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' -Cups           ' + str(totalBrought(allGuests, 'cups')))
umber of things being brough:')
print(' -Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' -Ham Sandwhiches' + str(totalBrought(allGuests, 'ham sandwhiches')))
print(' -Apples Pies    ' + str(totalBrought(allGuests, 'apple pies')))