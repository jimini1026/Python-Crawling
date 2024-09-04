import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/field_submit.naver?menu=market_sum&returnUrl=http://finance.naver.com/sise/sise_market_sum.naver?&page=1&fieldIds=per&fieldIds=roe&fieldIds=pbr&fieldIds=reserve_ratio"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")

trs = soup.select('.type_2 > tbody > tr[onmouseover="mouseOver(this)"]')
for tr in trs:
    # nth-of-type 사용
    name = tr.select_one("td:nth-of-type(2)").text
    per = tr.select_one("td:nth-of-type(7)").text
    roe = tr.select_one("td:nth-of-type(8)").text
    pbr = tr.select_one("td:nth-of-type(9)").text
    reserve_ratio = tr.select_one("td:nth-of-type(10)").text
    print(name, per, roe, pbr, reserve_ratio)