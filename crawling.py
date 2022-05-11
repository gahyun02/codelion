from bs4 import BeautifulSoup  #from (모듈 이름) import (기능)
import requests
from datetime import datetime

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}  # 일반적 유저임을 보여주는 코드
url = "https://datalab.naver.com/keyword/realtimeList.naver?age=20s"  # ?전은 공통부분이고, ?후는 파라미터로 실시간 검색어를 20대 기준으로 나타낸 것임.
response = requests.get(url) 
soup = BeautifulSoup(response.text, 'html.parser')  # BeautifulSoup(데이터, 파싱방법)-> HTML, XML 파일 가져올 수 있음

rank = 1
# span - item_title
results = soup.findAll('span','item_title')  # html 문서에서 모든 span 태그를 가져옴

print(response.text)

search_rank_file = open("rankresult.txt","a")

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

for result in results:
    search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
    print(rank,"위 : ",result.get_text(),"\n")
    rank += 1