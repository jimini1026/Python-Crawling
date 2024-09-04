from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import urllib.request
import pyautogui

keyword = pyautogui.prompt("검색어를 입력하세요 >>>")

if not os.path.exists(f"05_네이버_이미지_크롤링/{keyword}"):
    os.mkdir(f"05_네이버_이미지_크롤링/{keyword}")

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path = ChromeDriverManager().install())
browser = webdriver.Chrome(service = service, options = chrome_options)

url = f"https://search.naver.com/search.naver?where=image&sm=tab_jum&query={keyword}"
browser.implicitly_wait(10)
browser.maximize_window()
browser.get(url)

# 스크롤 전 높이
before_h = browser.execute_script("return window.scrollY")

# 무한 스크롤
while True:
    # 맨 아래로 스크롤 내리기
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(5)

    # 스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h:
        break
    before_h = after_h

# 이미지 태그 추출
imgs = browser.find_elements(By.CSS_SELECTOR, "._image._listImage") # 자료형은 리스트

for i, img in enumerate(imgs, 1):
    # 각 이미지 태그의 주소
    img_src = img.get_attribute("src")
    print(i, img_src)
    urllib.request.urlretrieve(img_src, f"05_네이버_이미지_크롤링/{keyword}/{i}.png")
