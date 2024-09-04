from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path = ChromeDriverManager().install())
browser = webdriver.Chrome(service = service, options = chrome_options)

url = "https://map.naver.com/v5/?c=15,0,0,0,dh"
browser.implicitly_wait(10)
browser.maximize_window()
browser.get(url)

# 종종 아이디 값이 바뀌는 사이트가 존재
search = browser.find_element(By.CSS_SELECTOR, "input.input_search")
search.click()
time.sleep(1)
search.send_keys("서울 게스트하우스")
time.sleep(1)
search.send_keys(Keys.ENTER)
time.sleep(2)

# iframe 안으로 들어가기
browser.switch_to.frame("searchIframe")

# iframe 안 쪽을 한 번 클릭하기
browser.find_element(By.CSS_SELECTOR, "#_pcmap_list_scroll_container").click()

# 로딩된 데이터 개수 확인
lis = browser.find_elements(By.CSS_SELECTOR, "li.UEzoS")
before_len = len(lis)

while True:
    # 맨 아래로 스크롤 내린다.
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(1.5)

    # 스크롤 후 로딩된 데이터 개수 확인
    lis = browser.find_elements(By.CSS_SELECTOR, "li.UEzoS")
    after_len = len(lis)

    # 로딩된 데이터 개수가 같다면 반복 멈춤
    if before_len == after_len:
        break
    before_len = after_len

# 데이터 기다리는 시간 0 (데이터 없더라도 빨리 넘어감)
browser.implicitly_wait(0)

for li in lis:
    # 별점 있는 것만 크롤링
    if len(li.find_elements(By.CSS_SELECTOR, "span.XGoTG._Lt3N > em")) > 0:
        # 가게명
        name = li.find_element(By.CSS_SELECTOR, "span.place_bluelink").text
        # 별점
        star = li.find_element(By.CSS_SELECTOR, "span.XGoTG._Lt3N > em").text

        print(name, star)