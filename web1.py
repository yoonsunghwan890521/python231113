#web1.py
from bs4 import BeautifulSoup

#페이지 로딩
page = open("test01.html","rt", encoding="utf-8").read()

#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")

#전체 페이지 보기
#print(soup.prettify())

#<p>전체를 검색
#print(soup.find_all("p"))

#첫번째 <p>만 검색
#print(soup.find("p"))

#조건검색 : <p class="outer-text">
#print(soup.find_all("p",class_="outer-text"))

#attrs 속성
#print(soup.find_all("p", attrs={"class":"outer-text"}))

#<p id="first">
#print(soup.find_all("p",id="first"))

#태그 안쪽의 컨텐츠만 출력: .text 속성
for tag in soup.find_all("p"):
    title = tag.text.strip()
    print(title)


