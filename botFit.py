# coding=utf-8

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import time
import credentials

classId = '' # Id for onclick recognition

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("http://www.aimharder.com/login")

print(browser.find_element_by_name('mail'))
browser.find_element_by_name('mail').send_keys(credentials.ah_pwd)
browser.find_element_by_name('pw').send_keys(credentials.ah_pwd)
browser.find_element_by_name('login').click()

browser.get("https://crossfitsantmarti.aimharder.com/schedule")
time.sleep(2)

try:
    browser.find_element_by_class_name('ui-dialog-titlebar-close ui-corner-all').click()
except:
    print('No dialog showed')


browser.find_element_by_id('nextDay').click()
time.sleep(2)

now = datetime.now()
current_time = now.strftime("%H:%M")
while current_time == '22:00':
    now = datetime.now()
    current_time = now.strftime("%H:%M")

browser.find_element_by_xpath("//a[@onclick='bookClass(" + classId + ", this, 0);']").click()
browser.quit()