###----------------------------------------------------###
###                CH. 11 Web Scraping                 ###
###----------------------------------------------------###


#Web scraping - using a program to download and process content from the Web
    #Google runs many web scraping programs for all the searches it conducts.

#3 main modules
    
    #webbrowser - Opens a browser to a specific page 
    #Requests - Downloads files and web pages from the Internet
    #Beautiful Soup - Parses HTML, the format that web pages are written in
    #Selenium - Lanches and controls a web browser. Selenium is able to fill in forms and simulate mouse clicks in this browser
    
import webbrowser
webbrowser.open('http://inventwithpython.com/')

### Downloading Files from the Web with the Request module

#Request mod lets you download files from web
    #ignores network errors, connection problems and data compression
    
#requests.get() takes a string of a URL to download
#calling type() on a request.get() you can see it returns a Response object
    #this contains the response that the web server gave for your request

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)

res.status_code == requests.codes.ok

len(res.text)

print(res.text[:250])

### Checking for Errors
#raise_for_status() will raise an exception if error dl-ing file and will do nothing if dl succeeds
import requests
res = requests.get('https://inventwithpython.com/page_that_does_not_extist')
res.raise_for_status()

#if not a big deal if dl doesn't occur wrap raise_for_status() with try/except statements
import requests
res = requests.get('https://inventwithpython.com/page_that_does_not_extist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))


### Saving Downloaded Files to the Harddrive
#you can save web page to a file w/ standard open() and write() methods
    #must write in binary mode
        # 'wb'as second argument to open()

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('C:\\Users\\ejmil\\source\\repos\\AutoTheBoringStuff\\RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()

### Viewing browsers HTML info
# can right click and click view page source
# can press f12 to view developer tools
    #can hilight and right click items and click inspect to jump to source code for highlighted item

###Creating a BeautifulSoup Object from HTML
#The bs4.BeautifulSoup() function must be called with a string containing the HTML it will parse
    #it will return a Beautiful Soup object

import requests, bs4
res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup)

ExampleFile = open('C:\\Users\\ejmil\\source\\repos\\AutoTheBoringStuff\\11htmldocexample.html')
exampleSoup = bs4.BeautifulSoup(ExampleFile)
type(exampleSoup)

#once you have a bs4 object you can use its methods and functions to locate specific HTML elements

###Finding an Element with the Select() method
#pass a string of CSS selector for the element you are looking for
    #selectors are like regex because the specify a pattern to look for


#Selector Passed to the             #will match
#select() method
"""
soup.select('div')                  All elements named <div>

soup.select('#author')              The element with an id attribute of author

soup.select('.notice')              All elements that use a CSS class attribute named notice

soup.select('div span')             All elements named <span> that are within an element named <div>

soup.select('div > span')           All elements named <span> that are directly within an element named <div>, with no other element in between

soup.select('input[name]')          All elements named <input> that have a name attribute with any value

soup.select('input[type="button"]') All elements named <input> that have an attribute named type with value button
"""

import bs4
exampleFile = open('C:\\Users\\ejmil\\source\\repos\\AutoTheBoringStuff\\11htmldocexample.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select('#author')
type(elems)
len(elems)
type(elems[0])
elems[0].getText()
str(elems[0])
elems[0].attrs

#code will pull id="author" out of example HTML
    #used select('#author') to return a list of all elements with id="author"
    #stored the list of Tag objects as elems
    #len(elem) told us how many Tags there were
    #getText() gets the raw text of the Tag
    #elem[0] returns strings with starting and closing tags + raw text
    #attrs gives a dictionary  of id and author


pElems = exampleSoup.select('p')
str(pElems[0])
pElems[0].getText()
str(pElems[1])
pElems[1].getText()
str(pElems[2])
pElems[2].getText()

###Getting data from an Element's Attributes
#get() method for Tag objects allows access to attribute values from an element
import bs4
soup = bs4.BeautifulSoup(open('C:\\Users\\ejmil\\source\\repos\\AutoTheBoringStuff\\11htmldocexample.html'))
spanElem = soup.select('span')[0]
str(spanElem)
spanElem.get('id')
spanElem.get('some_nonexistent_addr') == None
spanElem.attrs

###Controlling the Browser with the Selenium Mod###
#Programmatically clicks links and fills in login information
    #Often slow; reserved for more complicated tasks

### Starting a Selenium-controlled Browser ###
from selenium import webdriver
browser = webdriver.Firefox()
type(browser)
browser.get('http://inventwithpython.com')

#webdriver.ur_browser_here creates a Webdriver object

### Finding Elements on the Page ###

#find_element_* and find_elements_*
    #finds a single element and finds all elements respectively

#Methods                                     #Description
#find_element(s)_by_class_name(name)         #Element that uses CSS class 'name'

#find_element(s)_by_css_selector(selector)   #Elements that match the CSS 'selector'

#find_element(s)_by_id(id)                   #Elements with a matching id attribute value

#find_element(s)_by_link_text(text)          #<a> elements that completely match the text provided

#find_element(s)_by_partial_link_text(text)  #<a> elements that contain the text provided

#find_element(s)_by_name(name)               #Elements with a matching name attribute value

#find_elements_by_tag_name(name)             #Elements with a matching tag name (case insensitive; an <a> element is matched by 'a' and 'A')

#all arguments to the methods are case sensitive
    #*_by_tag_name() is the only exception
    
#if no element exists then selenium will raise a NoSuchElement exception
    #try/except statements are needed if you don't want this error to crash the program

#once you have a WebElement object the following attributes/methods will give you more info

#attribute/method               #Description
#tag_name                       #The tag name such as 'a' for an <a> element

#get_attribute(name)            #The value for the elemnt's name attribute

#text                           #the text within the element, such as 'hello' in <span>hello</span>

#clear()                        #For the text field or text area elements, clears the text typed into it

#is_displayed()                 #Returns True if the element is visible; otherwise returns False

#is_enabled()                   #For input elements, returns True if the element is enabled; otherwise returns False

#is_selected()                  #For checkbox or radio button elements, returns True if the element is selected; otherwise returns False

#location                       #A dictionary with keys 'x' and 'y' for the position of the element in the page


