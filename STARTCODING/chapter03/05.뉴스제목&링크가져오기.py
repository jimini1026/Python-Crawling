import requests
from bs4 import BeautifulSoup

response = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90")
html = response.text #웹사이트 전체 정보를 가져옴
#HTML 텍스트 가져오기 쉽게 soup 만들기(html이 문자열 코드이기에 파싱하기 쉽게 soup 만듦)

soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".news_tit") #결과가 리스트로 나옴

for link in links:
    title = link.text #태그 안에 텍스트 요소 가져옴
    url = link.attrs['href'] #href의 속성값 가져옴
    print(title, url)