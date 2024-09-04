from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service = service, options = chrome_options)

driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://shopping.naver.com/home")
time.sleep(2)

# 검색창 클릭
search = driver.find_element(By.CSS_SELECTOR, "input._searchInput_search_text_3CUDs")
search.click()

# 검색어 입력
search.send_keys("아이폰 13")
search.send_keys(Keys.ENTER)
