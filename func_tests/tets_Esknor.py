from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.get('http://esknor.pythonanywhere.com/')

assert 'Django' in browser.title

print (browser.title)

try:

    WebDriverWait(browser, 10).until(EC.title_contains("Welcome"))

    # You should see "Welcome to Django This is my cool Site!"
    print (browser.title,' This is my cool Site!')

finally:
    browser.quit()