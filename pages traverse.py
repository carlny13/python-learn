from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://detail.zol.com.cn/cell_phone_index/subcate57_0_list_1_0_1_2_0_2.html")
bsObj = BeautifulSoup(html.read())


html = '''<a href="some_url">next</a>
<span class="class"><a href="another_url">later</a></span>'''
soup = BeautifulSoup(html)
for a in soup.find_all('a', href=True):
    print ("Found the URL:", a['href'])
