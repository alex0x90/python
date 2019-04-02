from selenium import webdriver


import time

#Locate the driver
chromedriver = 'chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

#Make a browser and open url in it
browser = webdriver.Chrome(chromedriver, options=options)
#Enter URL to Open
browser.get('https:\\facebook.com')

#Find stuff where the attribute is X and save them to variable
username = browser.find_element_by_name("user")
password = browser.find_element_by_name("password")

#Insert in the stuff found the following value attribute to perform a login
username.send_keys("test@gmail.com")
password.send_keys("test1234")


#Press a button,
#search for button parameters to click >
time.sleep(3)
browser.find_element_by_css_selector("#values").click()

#Wait until certain popup window will show, if not for 10 seconds, go next.

for wait in range(0,20):

    time.sleep(0.5)
    try:
        browser.find_element_by_css_selector("#values").click()
        break
    except:
        pass


browser.find_element_by_css_selector('#go to specific page').click()

