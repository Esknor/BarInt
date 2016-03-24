from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.get('http://esknor.pythonanywhere.com/')

assert 'Welcome to Django' in browser.title

print (browser.title)

try:

    WebDriverWait(browser, 10).until(EC.title_contains("Django"))

    print (browser.title)

finally:
    browser.quit()