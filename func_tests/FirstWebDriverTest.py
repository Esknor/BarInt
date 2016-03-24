from webbrowser import browser
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.google.com.ua/')
body = browser.find_element_by_tag_name('body')

assert 'Google' in body.text
print('Hello Google')

browser.quit()