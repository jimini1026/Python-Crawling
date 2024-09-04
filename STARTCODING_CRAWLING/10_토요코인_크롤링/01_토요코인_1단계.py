import requests
from bs4 import BeautifulSoup

url = 'https://www.toyoko-inn.com/korea/search/reserve/room'

header = {
    'Host': 'www.coupang.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
}

response = requests.get(url, headers = header)
html = response.text
soup = BeautifulSoup(html, "html.parser")
beds = soup.select("ul.btnLink03")
print(beds)