# python-learn

上传文件路径为何需要使用双斜杠 
平时我们上传文件，读取文件时，路径的编写有两种方式，使用双斜杠“\\”，或者正斜杠“/”
例如：

("D:\\test\\bb\\1.txt")

("D:/test/bb/1.txt")

为什么要使用双斜杠原因为：

由于我们是把路径当成是一个字符串传进去的，在字符串中斜杠“\”被当做转义字符识别，所以要用“\\”才能表示一个斜杠。
searchUrl = "http://ks.pconline.com.cn/product.shtml?"
phone_id_name = "E:\python\\ueprice_crawler\phone.txt"

抓页面时要注意一下selector，

读文件，打印文件
f = open('E:\python\ueprice_crawler\phone_price4.txt', 'r')
print f.read()


爬虫：
#提取页面信息
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://detail.zol.com.cn/cell_phone/index398689.shtml")
bsObj = BeautifulSoup(html.read())
print(bsObj.h1.text,bsObj.h3.span.text,bsObj.script.text) #提取标题\上市时间\URL

from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://detail.zol.com.cn/cell_phone/index398689.shtml")
bs0bj=BeautifulSoup(html)
priceList=bs0bj.find_all("div",{"class":{"price-normal","total-score"}})
for price in priceList:
    print(price.get_text()) #提取价格信息\评分
    
    
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


