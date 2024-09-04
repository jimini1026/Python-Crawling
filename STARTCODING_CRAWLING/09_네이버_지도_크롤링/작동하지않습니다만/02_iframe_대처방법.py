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
search.send_keys("강남역 맛집")
time.sleep(1)
search.send_keys(Keys.ENTER)
time.sleep(2)

# iframe 안으로 들어가기
browser.switch_to.frame("searchIframe")

# 가게 10개 가져오기
names = browser.find_elements(By.CSS_SELECTOR, ".place_bluelink.TYaxT")
for name in names:
    print(name.text)