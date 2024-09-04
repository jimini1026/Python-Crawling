import requests
from bs4 import BeautifulSoup
import time
import openpyxl

wb = openpyxl.Workbook()
ws = wb.create_sheet("주식")
ws.append(["종목명", "PER", "ROE", "PBR", "유보율"])

pages = 10
for page in range(1, pages + 1):
    url = f"https://finance.naver.com/sise/field_submit.naver?menu=market_sum&returnUrl=http://finance.naver.com/sise/sise_market_sum.naver?page={page}&fieldIds=per&fieldIds=roe&fieldIds=pbr&fieldIds=reserve_ratio"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    stocks = soup.select(".type_2 > tbody > tr")
    for stock in stocks:
        try:
            name = stock.select_one("td:nth-of-type(2)").text
            PER = stock.select_one("td:nth-of-type(7)").text
            ROE = stock.select_one("td:nth-of-type(8)").text
            PBR = stock.select_one("td:nth-of-type(9)").text
            reserve_ratio = stock.select_one("td:nth-of-type(10)").text
            print(name, PER, ROE, PBR, reserve_ratio)
            ws.append([name, PER, ROE, PBR, reserve_ratio])
        except:
            continue
    time.sleep(3)

wb.save("08_네이버_금융_크롤링/주식_정리.xlsx")