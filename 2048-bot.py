#! python3
# 2048-bot.py - plays 2048 in browser by pressing arrow keys
from multiprocessing.connection import wait
import requests, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# main code:
browser = webdriver.Safari()
browser.get('https://play2048.co')
htmlElem = browser.find_element_by_tag_name('html')
while True:
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)

