from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import openpyxl

wb = openpyxl.Workbook()
ws = wb.create_sheet("네이버_지도_크롤링")
ws.append(["순위", "이름", "별점", "리뷰 수"])

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path = ChromeDriverManager().install())
browser = webdriver.Chrome(service = service, options = chrome_options)

url = "https://map.naver.com/v5/?c=15,0,0,0,dh"
browser.implicitly_wait(10)
browser.maximize_window()
browser.get(url)

search = browser.find_element(By.CSS_SELECTOR, "input.input_search")
search.click()
time.sleep(1)
search.send_keys("서울 게스트하우스")
time.sleep(1)
search.send_keys(Keys.ENTER)

browser.switch_to.frame("searchIframe")

browser.find_element(By.CSS_SELECTOR, "#_pcmap_list_scroll_container").click()

lis = browser.find_elements(By.CSS_SELECTOR, "li.Fh8nG.D5NxL")
before_len = len(lis)

while True:
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
    time.sleep(2)
    after_len = len(browser.find_elements(By.CSS_SELECTOR, "li.Fh8nG.D5NxL"))

    if before_len == after_len:
        break
    before_len = after_len

browser.implicitly_wait(0)
time.sleep(3)
lis = browser.find_elements(By.CSS_SELECTOR, "li.Fh8nG.D5NxL")

for i, li in enumerate(lis, 1):
    try:
        name = li.find_element(By.CSS_SELECTOR, ".place_bluelink.moQ_p").text
        star = li.find_element(By.CSS_SELECTOR, "span.XGoTG._Lt3N > em").text
        review = li.find_element(By.CSS_SELECTOR, "span.XGoTG.wy6zf").text

    except:
        continue

    print(i, name, star, review)
    ws.append([i, name, star, review])

wb.save("09_네이버_지도_크롤링/네이버_지도_크롤링.xlsx")