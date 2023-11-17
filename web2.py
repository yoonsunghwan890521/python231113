# web2.py
# 웹서버와 통신을 위한 requests 모듈 import
import requests

# 웹 페이지 크롤링을 위한 BeautifulSoup 모듈 import
from bs4 import BeautifulSoup

# 대당 마켓(fleamarket)의 URL
url = "https://www.daangn.com/fleamarket/"

# 해당 URL에 GET 요청을 보내서 응답을 받음
response = requests.get(url)

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(response.text, "html.parser")

# 게시물들을 담고 있는 div 태그들을 찾아서 리스트로 저장
posts = soup.find_all("div", attrs={"class": "card-desc"})

# 결과를 저장할 텍스트 파일 열기
f = open("dangn.txt", "wt", encoding="utf-8")

# 각 게시물에 대한 정보를 추출하고 텍스트 파일에 저장
for post in posts:
    # 제목 추출
    title = post.find("h2", attrs={"class": "card-title"})
    
    # 가격 추출
    price = post.find("div", attrs={"class": "card-price"})
    
    # 위치 추출
    addr = post.find("div", attrs={"class": "card-region-name"})
    
    # 추출한 정보에서 줄바꿈 문자 제거
    title = title.text.replace("\n", "")
    price = price.text.replace("\n", "")
    addr = addr.text.replace("\n", "")
    
    # 화면에 출력
    print("{0},{1},{2}".format(title, price, addr))
    
    # 파일에 쓰기
    f.write(f"{title},{price},{addr}\n")

# 파일 닫기
f.close()



# 원 사이트 코드를 보고 추측함!!
# <div class="card-desc">
#       <h2 class="card-title">삼성텔레비전65인치</h2>
#       <div class="card-price ">
#         150,000원
#       </div>
#       <div class="card-region-name">
#         서울 서초구 반포2동
#       </div>
#       <div class="card-counts">
#           <span>
#             관심 29
#           </span>
#         ∙
#         <span>
#             채팅 34
#           </span>
#       </div>
#     </div>