from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time
driver = webdriver.Chrome()
driver.get("https://www.naver.com")
time.sleep(30)
