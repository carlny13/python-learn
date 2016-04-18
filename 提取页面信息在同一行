from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://detail.zol.com.cn/cell_phone/index398689.shtml")
bsObj = BeautifulSoup(html.read())

priceList=bsObj.find_all("div",{"class":"price-normal"})
for price in priceList:
    price1=(price.get_text()) #/价格信息
priceList1=bsObj.find_all("div",{"class":"total-score"})
for score in priceList1:
    score1=(score.strong.get_text()) #/评分信息
result1=bsObj.h1.text+","+bsObj.h3.span.text+","+bsObj.script.text  #提取标题\上市时间\URL
print(result1+","+price1+","+score1)
