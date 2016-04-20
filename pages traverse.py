#py3.5
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://detail.zol.com.cn/cell_phone_index/subcate57_0_list_1_0_1_2_0_2.html")
bsObj = BeautifulSoup(html.read())


html = '''<a href="some_url">next</a>
<span class="class"><a href="another_url">later</a></span>'''
soup = BeautifulSoup(html)
for a in soup.find_all('a', href=True):
    print ("Found the URL:", a['href'])

# 提取上一页URL
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://detail.zol.com.cn/cell_phone_index/subcate57_0_list_1_0_1_2_0_2.html")
bsObj = BeautifulSoup(html.read())

pageList=bsObj.find_all("div",{"class":"small-page"})
for page in pageList:
    print(page.a['href']) #/页面信息
    
# 提取下一页URL
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://detail.zol.com.cn/cell_phone_index/subcate57_list_1.html?")
bsObj = BeautifulSoup(html.read())

pageList=bsObj.find_all("a",{"class":"small-page-next"})
for page in pageList:
    print(page['href']) #/页面信息
    
#提取下一页到列表：
from urllib.request import urlopen
from bs4 import BeautifulSoup
import  re

pages=set()
def getLinks(pageUrl):
    global pages
    html=urlopen("http://detail.zol.com.cn/cell_phone_index/subcate57_list_1.html?"+pageUrl)
    bsObj=BeautifulSoup(html)
    for link in bsObj.findAll("a",{"class":"small-page-next"}):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #我们遇到了新的页面
                newPage=link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks("")


#尝试遍历输出：
#coding=utf-8

from bs4 import  BeautifulSoup
import  urllib2
import re
Items=[]
for pages in range(2,105):
    if pages==0:
        url="http://detail.zol.com.cn/cell_phone_index/subcate57_list_1.html?"
    else :
        url="http://detail.zol.com.cn/cell_phone_index/subcate57_0_list_1_0_1_2_0_"+str(pages)+".html"
    try:
        html=urllib2.urlopen(url)
        bsObj=BeautifulSoup(html)
        #print bsObj.h1.text.encode('utf-8')
        priceList=bsObj.find_all("div",{"class":"price-normal"})
        for price in priceList:
            price1=(price.get_text()) #/princ infomation
        priceList1=bsObj.find_all("div",{"class":"total-score"})
        for score in priceList1:
            score1=(score.strong.get_text()) #/score infomation
                #print type(price.get_text())
            text=bsObj.h1.text+","+bsObj.h3.span.text+" ,"+bsObj.script.text +","+price.get_text()+","+score.strong.get_text()
                #print result.encode('utf-8')
            Items.append(text)
    except:
        continue
f=open("F:/zlo_test1.txt","w")
for n in Items:
    f.write(n)
print len(Items)
