from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://detail.zol.com.cn/cell_phone_index/subcate57_list_1.html?")
bsObj = BeautifulSoup(html.read())

priceList=bsObj.find_all("div",{"class":"price-normal"})
for price in priceList:
    price1=(price.get_text()) #/价格信息
priceList1=bsObj.find_all("div",{"class":"total-score"})
for score in priceList1:
    score1=(score.strong.get_text()) #/评分信息
result1=bsObj.h1.text+","+bsObj.h3.span.text+","+bsObj.script.text  #提取标题\上市时间\URL
print(result1+","+price1+","+score1)

#上面代码把要提取的5个信息放在同一行输入，且逗号分隔.

或者这样也行，减少几行代码：
from urllib.request import urlopen 
from bs4 import BeautifulSoup 
html = urlopen("http://detail.zol.com.cn/cell_phone/index398689.shtml") bsObj = BeautifulSoup(html.read())

priceList=bsObj.find_all("div",{"class":"price-normal"}) 
for price in priceList: 
price1=(price.get_text()) #/价格信息 
priceList1=bsObj.find_all("div",{"class":"total-score"}) 
for score in priceList1: 
score1=(score.strong.get_text()) #/评分信息 
result1=bsObj.h1.text+","+bsObj.h3.span.text+","+bsObj.script.text 
#提取标题\上市时间\URL 
print(result1+","+price1+","+score1)

执行单页面爬虫：

__author__ = ''
#coding=utf-8

from bs4 import  BeautifulSoup
import  urllib2
import re

url="http://detail.zol.com.cn/cell_phone_index/subcate57_list_1.html?"

html=urllib2.urlopen(url)
objbs=BeautifulSoup(html)
s=objbs.find_all('div',{'id' : "J_BrandAll"})
file=open("D:/telephone_1.txt",'wb')
count=0

for i in s:
    test=i.find_all('a')
    for link in test:
        url_list= "http://detail.zol.com.cn"+link.get('href')
        html_list=urllib2.urlopen(url_list).read()
        link_list=re.findall('<a href="(.*?)" class="pic"',html_list)
        for link_telephon in link_list:
            link_telephon_pic="http://detail.zol.com.cn"+link_telephon
            html1 = urllib2.urlopen(link_telephon_pic)
            bsObj = BeautifulSoup(html1.read())
            #print bsObj.h1.text+" "+bsObj.h3.span.text+"  "+bsObj.script.text #提取标题\上市时间\URL
            #print bsObj.h1.text.encode('utf-8')
            priceList=bsObj.find_all("div",{"class":{"price-normal","total-score"}})
            for price in priceList:
                count+=1
                print count
                #print type(price.get_text())
            result=bsObj.h1.text+" "+bsObj.h3.span.text+"  "+bsObj.script.text +" "+price.get_text() #提取价格信息\评分
                #print result.encode('utf-8')
            file.write(result.encode('utf-8')+"\n")
            

改进后，单页面link抓取，输出结果在同一行，且逗号分隔：

#coding=utf-8

from bs4 import  BeautifulSoup
import  urllib2
import re

url="http://detail.zol.com.cn/cell_phone_index/subcate57_list_1.html?"

html=urllib2.urlopen(url)
objbs=BeautifulSoup(html)
s=objbs.find_all('div',{'id' : "J_BrandAll"})
file=open("D:/telephone_2.txt",'wb')
count=0

for i in s:
    test=i.find_all('a')
    for link in test:
        url_list= "http://detail.zol.com.cn"+link.get('href')
        html_list=urllib2.urlopen(url_list).read()
        link_list=re.findall('<a href="(.*?)" class="pic"',html_list)
        for link_telephon in link_list:
            link_telephon_pic="http://detail.zol.com.cn"+link_telephon
            html1 = urllib2.urlopen(link_telephon_pic)
            bsObj = BeautifulSoup(html1.read())
            #print bsObj.h1.text.encode('utf-8')
            priceList=bsObj.find_all("div",{"class":"price-normal"})
            for price in priceList:
                price1=(price.get_text()) #/princ infomation

            priceList1=bsObj.find_all("div",{"class":"total-score"})
            for score in priceList1:
                score1=(score.strong.get_text()) #/score infomation
                count+=1
                print count
                #print type(price.get_text())
            result=bsObj.h1.text+","+bsObj.h3.span.text+" ,"+bsObj.script.text +","+price.get_text()+","+score.strong.get_text()
                #print result.encode('utf-8')
            file.write(result.encode('utf-8')+"\n")
