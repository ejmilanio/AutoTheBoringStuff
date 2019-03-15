"""

Project: Multi-Clipboard

1) Check the command line for keywords
    a) if arg is SAVE, the clipboard contents are saved
    b) if arg is LIST, then all keywords are copied to clipboard
    c) else text is copied to the clipboard

"""
#! python3
# 7multiClipboard.pyw - Saves and loads pieces of text to the clipbaord
# Usage: py.exe mcb.pyw save <keyword> - Saves clipbaord to keyword
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#        py.exe mb.pyw list - Loads all keywords to clipboard

import shelve, pyperclip, sys

#creates a shelf for the variable mcbShelf
mcbShelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    #List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        
mcbShelf.close()
