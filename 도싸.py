# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(1,11):
        #도싸의 중고장터 주소 
        data ='https://www.corearoadbike.com/board/board.php?g_id=recycle02&t_id=Menu01Top6&category=%ED%8C%90%EB%A7%A4&page=' + str(n)
        #print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')   
        list = soup.find_all('td', attrs={'class':'list_title_B'})

#<td class="list_title_B"><img src="/img/board_bt_order_r.gif" align="absmiddle" title="재등록물품"> <font color="#666666">[판매 디스크]</font> 
# <a href="./board.php?g_id=recycle02&amp;t_id=Menu01Top6&amp;category=%ED%8C%90%EB%A7%A4&amp;page=2&amp;no=1171795" title="23 서벨로 cervelo s5 48"><font color="#000000">23 서벨로 cervelo s5 48</font></a><b><font class="num_cmt_3">1</font><b>&nbsp;<img src="/img/icon_photo.gif" align="absmiddle"></b></b></td>

# <td class="list_title_B"><img src="/img/board_bt_order_r.gif" align="absmiddle" title="재등록물품"> <font color="#666666">[판매 디스크]</font>
#  <a href="./board.php?g_id=recycle02&amp;t_id=Menu01Top6&amp;category=%ED%8C%90%EB%A7%A4&amp;page=3&amp;no=1172075" title="라피에르 젤리우스sl600 풀카본 로드자전거"><font color="#000000">라피에르 젤리우스sl600 풀카본 로드자전거</font></a><img src="/img/icon_photo.gif" align="absmiddle"></td>


        for item in list:
                try:
                        #앞뒤 공백 없애, "a"태그를 가져와 --> a href인 것을 찾는 것임
                        title = item.find("a").text.strip()
                        print(title)
                        # if (re.search('아이폰', title)):
                        #         print(title.strip())
                        #         print('https://www.clien.net'  + item['href'])
                except:
                        #에러처리하는 키워드임 (해주면 좋음)
                        pass
        
