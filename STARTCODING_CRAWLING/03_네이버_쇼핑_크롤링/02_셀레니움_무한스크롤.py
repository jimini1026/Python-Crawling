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

# 스크롤 전 높이
before_h = driver.execute_script("return window.scrollY") #자바 스크립트 명령어 실행 가능토록 함

# 무한 스크롤
while True:
    # 맨 아래로 스크롤 내린다.
    driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END) #End 키

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(1)

    # 스크롤 후 높이
    after_h = driver.execute_script("return window.scrollY")

    if after_h == before_h:
        break
    before_h = after_h

# 상품 정보 div
items = driver.find_elements(By.CSS_SELECTOR, "div.adProduct_info_area__dTSZf")

for item in items:
    name = item.find_element(By.CSS_SELECTOR,  "div.product_title__Mmw2K").text
    price = item.find_element(By.CSS_SELECTOR, ".price_num__S2p_v").text
    link = item.find_element(By.CSS_SELECTOR, "div.product_title__Mmw2K > a").get_attribute("href")
    print(name, price, link)