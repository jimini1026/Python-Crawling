import requests
from bs4 import BeautifulSoup
import time

url = 'https://www.toyoko-inn.com/korea/search'

data_obj = {
    "lcl_id": "ko",
    "prcssng_dvsn": "dtl",
    "sel_area_txt": "한국",
    "sel_htl_txt": "토요코인 서울강남", 
    "chck_in": "2023/07/16",
    "inn_date": "1",
    "sel_area": "8",
    "sel_htl": "00282",
    "rsrv_num": "1",
    "sel_ldgngPpl": "1" 
}

cnt = 1
while True:

    try:
        response = requests.post(url, data = data_obj)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        beds = soup.select("ul.btnLink03")

        for i, bed in enumerate(beds, 1):
            links = bed.select("a")
            if len(links) > 0:
                print(i, links)
                if i <= 5:
                    print("싱글 잔실 있음!")
                elif i <= 7:
                    print("더블 잔실 있음!")
                elif i <= 9:
                    print("트윈 잔실 있음!")
                elif i <= 11:
                    print("트리플 잔실 있음!")
                elif i <= 13:
                    print("하트풀트윈 잔실 있음!")

    except:
        print("오류 발생. 다시 시도")

    print(f"{cnt}번째 시도입니다.")
    time.sleep(10)
    cnt += 1