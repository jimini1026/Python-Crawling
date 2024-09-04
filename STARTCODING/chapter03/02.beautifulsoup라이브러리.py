import requests
from bs4 import BeautifulSoup

# naver 서버에 대화 시도
response = requests.get("https://www.naver.com/")

# naver 에서 html 줌
html = response.text

# html 번역 선생으로 수프 만듦
soup = BeautifulSoup(html, 'html.parser')

# id 값이 query인 놈 한개를 찾아냄
word = soup.select_one('#query')
#그냥 select는 여러 태그 선택


print(word)
#텍스트 요소만 출력하고 싶으면 print(word.text)