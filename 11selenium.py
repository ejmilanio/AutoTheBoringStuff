from selenium import webdriver

browser = webdriver.Chrome("C:\\Users\\Mike\\AppData\\Local\Programs\\Python\\Python37-32\\chromedriver_win32\\chromedriver.exe", service_args=["--verbose", "--log-path=D:\\qc1.log"])

browser.get('http://inventwithpython.com')
try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name!' % (elem.tag_name))

except:
    print('Was not able to find an element with that name')

     