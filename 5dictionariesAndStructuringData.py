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
    name = input
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
