from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager # 크롬 드라이버 자동 업데이트
from selenium.webdriver.common.keys import Keys

import time
import pyautogui
import pyperclip

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path = ChromeDriverManager().install())
browser = webdriver.Chrome(service = service, options = chrome_options)

url = "https://map.naver.com/v5/?c=15,0,0,0,dh"
browser.implicitly_wait(10)
browser.maximize_window()
browser.get(url)

search = browser.find_element(By.CSS_SELECTOR,"input.input_search")
search.click()
time.sleep(1)
search.send_keys("제주 게스트하우스")
time.sleep(1)
search.send_keys(Keys.ENTER)
time.sleep(1)


# iframe 안으로 들어가기
browser.switch_to.frame("searchIframe")

# iframe 나올 때
# browser.switch_to.default_content()

# 무한스크롤 하기
## iframe 안쪽을 한번 클릭하기
browser.find_element(By.CSS_SELECTOR,"#_pcmap_list_scroll_container").click()

## 로딩된 데이터 갯수 확인
lis = browser.find_elements(By.CSS_SELECTOR,"li.Fh8nG.D5NxL")
before_len = len(lis)

while True :
    # 맨 아래로 스크롤을 내린다.
    browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.END)
    # 페이지 로딩 시간을 준다
    time.sleep(1.5)
    # 스크롤 후 로딩된 데이터 개수 확인
    lis = browser.find_elements(By.CSS_SELECTOR,"li.Fh8nG.D5NxL")
    after_len = len(lis)
    
    # 로딩된 데이터 개수가 같다면 반복 멈춤
    if before_len == after_len:
        break
    before_len = after_len
    
# 데이터 수집
## lis에 모든 가계의 정보가 담겨있음
   
for li in lis:
    # 별점 있는 것만 선택
    try:
        stars = browser.find_elements(By.CSS_SELECTOR,"span.XGoTG.cN3MU> em")
        if len(stars)>0:
            # 가계이름
            store_name = li.find_element(By.CSS_SELECTOR,"span.place_bluelink.moQ_p").text 
            star_point = li.find_element(By.CSS_SELECTOR,"span.XGoTG.cN3MU> em").text
            print(store_name, star_point)
    except:
        continue
