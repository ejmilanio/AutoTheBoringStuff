###Debugging Ch. 10###
#Logging and Assertions are two early detection techniques
#Debugger, a feature in IDLE
    #Executes code one line at a time giving you a chance to inspect the values in variables as the code runs

###Raising Exceptions
#raise statement consists of 3 parts
    #1 raise keyword
    #2 call to the Exception() function
    #3 string with a helpful error message passsed to the Exception() function

raise Exception('This is the error message.')

#if no try and except statements that cover the raise statement, script will crash and raise error message
#will often see raise statements inbedded in the function

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string')
    if width <= 2:
        raise Exception('Width must be greater than 2')
    if height <= 2:
        raise Exception('Height must be greater than 2')
    print(symbol * width)
    for i in range (height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

for sym, w, h in (('*', 4, 4), ('O', 20, 6), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err) + ' for ' + sym)

#you can use raise Exception, try and except statemetns to gracefully handle errors


###Getting the Traceback as a string
#When python encounters an error it produces a Traceback
    #includes
        #erorr message
        #line number of error
        #the sequence of the function calls that led to the error

def spam():
    bacon()
def bacon():
    raise Exception('This is the error message')

spam()

#traceback is displayed when raised exception goes unhandled
#traceback.format_exc(). can also call a traceback as a string
    #useful for when you want an except statement to handle the exception
    #and need the traceback info

import traceback, os
os.chdir('C:\\Users\\ejmil\\source\\repos\\AutoTheBoringStuff')
try:
    raise Exception('This is the error message.')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The tracebackinfo was written to errorInfo.txt.')

#116 reps how many characters saved to the file

###Assertions
#a check to make sure code isn't doing something obviously wrong
    #consists of...
        #assert keyword
        #a condition (expression that evals True or False)
        #a comma
        #a string to display when the condition is False

podBayDoorStatus = 'open'
assert podBayDoorStatus == 'open', 'The po bay doors need to be "open".'
podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'

#assert means "this condition holds true, if not, there is a bug.
#assert statements should not be handled with try except statments
    #crashes program early as opposed to trying all try/except statments to the end
#for programmer errors, not user errors
    

market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
    for key in stoplight.keys():            #loops through all keys
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)   #immediately points out that a sanity check failed

switchLights(market_2nd)

#place -0 in the command line of a program to disable assertions

###Logging 
#the act of using the print() statement to understand what your program is outputting
#logging module creates a record of custom messages that you write
#log messages will describe when the prog execution has reached the logging function call and will list all variables you've specified
    #missing variables indicate parts of the script that was skipped

###-------------------------------------------------------------------------------
### run logging.basicConfig in IDLE on its own before running bits of code before testing other code
###-------------------------------------------------------------------------------
import logging
logging.basicConfig(level=logging.DEBUG, FORMAT =' %(asctime)s - %(levelname)s - %(messages)s') 

#logging.basicConfig() specifies what details about the log record you want to record and how you want them displayed
import logging, os
logging.basicConfig(level=logging.DEBUG, format=' %(asctimes)s - %(levelname)s - %(message)s')
logging.debug('Start of program')   

def factorial(n):
    logging.debug('Start of factorial(%s)' %(n))
    total = 1
    for i in range(1, n +1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' %(n))
    return total

print(factorial(5))
logging.debug('End of program')

#logging.debug(str) used when we want to print log information. 
    #Will call basicConfig() and a line of info will be printed.
    #Good to avoid having to retype print() statements
        #avoid removing print() statements because can just turn off in the end with logging.disable(logging.CRITICAL)

#intended for the programmer not the user

#Logging Levels


#   DEBUG      logging.debug()        #The lowest level. Used for the small details. Usually for diagnosing problems
#   INFO       logging.info()         #Used to record info on general events in your porgam or confirm things are working at certain points
#   WARNING    logging.warning()      #Used to indicate a potential problem may present a problem in the future
#   ERROR      logging.error()        #Used to record an error that cause the program to fail
#   CRITICAL   logging.critical()     #The highest level. Used to indicate a fatal error that caused the program to stop entirely.

#Its up to progammer to decide when and where to use these

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Some bugging detail')
logging.info('Some bugging info')
logging.warning('Some bug warning')
logging.error('Some bug error')
logging.critical('Something critical')

#by changing level=somelevel in the .basicConfig statment you can choose which levels to ignore
    #level=logging.WARNING, will only show WARNING, ERROR and CRITICAL.
        #It will skip DEBUG and INFO

###Disabling Logging
#logging.disable() will disable all logging functions
    #pass a logging level through logging.disable(HERE) to disable at that level and lower
        #logging.disable(logging.CRITICAL) will disable all logging

import logging
logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.critical('Critical Error! Critical Error')
logging.critical('Critical Error! Critical Error')
logging.error('Error! Error!')


###Logging to a file
#instead of displaying the logs to the screen you can save to a file
#use filename keyword argument

import logging, os

logging.basicConfig(filename='10myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('This should log')
logging.info('This should also')
logging.warning('Please log')


###IDLE's Debugger
#Debugger allows you to execute program one line at a time
#

