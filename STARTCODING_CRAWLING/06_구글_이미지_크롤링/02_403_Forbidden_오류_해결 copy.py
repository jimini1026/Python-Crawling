from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import urllib.request

if not os.path.exists("06_구글_이미지_크롤링/강아지"):
    os.mkdir("06_구글_이미지_크롤링/강아지")

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path = ChromeDriverManager().install())
browser = webdriver.Chrome(service = service, options = chrome_options)

url = "https://www.google.com/search?sxsrf=AB5stBhPwm9pxMuO98dR3Th6Rmml6VtFxA:1688983488721&q=%EA%B0%95%EC%95%84%EC%A7%80&tbm=isch&sa=X&ved=2ahUKEwj6tIHn8YOAAxW9Z_UHHbZrCtwQ0pQJegQICxAB&biw=1536&bih=754&dpr=1.25"
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
    time.sleep(1)

    # 스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h:
        break
    before_h = after_h

# 썸네일 이미지 태그 추출
imgs = browser.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd") # 자료형은 리스트

for i, img in enumerate(imgs, 1):
    # 이미지 클릭해서 큰 사이즈 찾기
    img.click()
    time.sleep(1)

    # 큰 이미지 주소 추출
    target = browser.find_element(By.CSS_SELECTOR, ".r48jcc.pT0Scc")
    img_src = target.get_attribute("src")

    # 이미지 다운로드
    # 크롤링 하다보면 HTTP Error 403: Forbidden 에러 발생
    opener = urllib.request.build_opener()
    opener.addheaders = [("User-Agent", "Mozila/5.0")]
    urllib.request.install_opener(opener)
    
    urllib.request.urlretrieve(img_src, f"06_구글_이미지_크롤링/강아지/{i}.jpg")