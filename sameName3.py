def spam():
    global eggs
    eggs = 'spam' #this is the global

def bacon():
    eggs = 'bacon' #this is a local
    print(eggs)

def ham():
    print(eggs) #will print the global

eggs = 42 #this is the global spam() will chage it's value from int(42) to str('spam')
spam()
print(eggs)
print(bacon())
print(ham())

# if you want to change a global var with a function you must precede that variable with a global statement
