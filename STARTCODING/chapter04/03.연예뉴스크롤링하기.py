import requests
from bs4 import BeautifulSoup
import time

response = requests.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EB%B8%94%EB%9E%99%ED%95%91%ED%81%AC&oquery=%EC%86%90%ED%9D%A5%EB%AF%BC&tqi=i6BwOlp0J1ZssNm3AWZssssssHl-329370")
html = response.text

soup = BeautifulSoup(html, "html.parser")
articles = soup.select("div.info_group") #뉴스 기사 10개 추출

for article in articles:
    links = article.select("a.info") #리스트
    if len(links) >= 2: 
        url = links[1].attrs["href"]
        response = requests.get(url, headers = {"User-agent":"Mozila/5.0"})
        html = response.text
        soup = BeautifulSoup(html, "html.parser")

        # 만약 연예 뉴스 라면
        if "entertain" in response.url:
            title = soup.select_one(".end_tit")
            content = soup.select_one("#articeBody")
        else:
            title = soup.select_one(".media_end_head_title")
            content = soup.select_one("#dic_area")

        print("==========링크==========\n", url)
        print("==========제목==========\n", title.text.strip())
        print("==========본문==========\n", content.text.strip())
        time.sleep(0.3)