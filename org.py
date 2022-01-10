import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
chrome = find("chrome.exe", "C:/")
cd = find("chromedriver.exe","C:/")
print(f"Found Chrome: {chrome}")
print(f"Found Chromedriver: {cd}")
option = webdriver.ChromeOptions()
option.binary_location = chrome
option.add_argument("start-maximized")
option.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2, 
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2, 
    "profile.default_content_setting_values.notifications": 1 
  })
browser = webdriver.Chrome(executable_path=cd, options=option)
browser.get("https://teams.microsoft.com")
time.sleep(5)
browser.find_element_by_xpath("//input[@type=\"email\"]")\
        .send_keys("") # ORGANIZATION EMAIL HERE
time.sleep(2)
browser.find_element_by_xpath('//input[@type="submit"]')\
        .click()
time.sleep(5)
browser.refresh()
time.sleep(5)
browser.find_element_by_xpath("//input[@type=\"text\"]")\
        .clear()
browser.find_element_by_xpath("//input[@type=\"text\"]")\
        .send_keys("") # ORGANIZATION USERNAME HERE
browser.find_element_by_xpath("//input[@type=\"password\"]")\
        .send_keys("") # ORGANIZATION PASSWORD HERE
time.sleep(2)
browser.find_element_by_xpath('//button[@type="submit"]')\
        .click()
time.sleep(2)
browser.find_element_by_xpath('//input[@type="submit"]')\
        .click()
element = WebDriverWait(browser, 10000000).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="toast-container"]/div[1]/div/div[3]/div/button[1]'))
        )
element.click()
time.sleep(5)
browser.find_element_by_xpath('//*[@id="ngdialog1"]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button')\
        .click()
