
from bs4 import BeautifulSoup
import  re
import urllib
import  urllib2
file=open("D:/telephone_4.txt",'wb')
count=0


for pages in range(1,106):
    if pages==0:
        url="http://detail.zol.com.cn/cell_phone_index/subcate57_0_list_1_0_1_2_0_0.html"
    else:
        url="http://detail.zol.com.cn/cell_phone_index/subcate57_0_list_1_0_1_2_0_"+str(pages)+".html"

    try:
        response = urllib2.urlopen(url)
        bsObj = BeautifulSoup(response.read())

        hrefList=bsObj.find_all("a",{"class":"pic"})
        for pageurl in hrefList:
            UEpage=(pageurl['href'])
            count+=1
            print(count)
            try:
                url_list= "http://detail.zol.com.cn"+UEpage
                html1 = urllib2.urlopen(url_list)
                bsObj = BeautifulSoup(html1.read())
                #print bsObj.h1.text.encode('utf-8')
                priceList=bsObj.find_all("div",{"class":"price-normal"})
                for price in priceList:
                    price1=(price.get_text()) #/princ infomation

                priceList1=bsObj.find_all("div",{"class":"total-score"})
                for score in priceList1:
                    score1=(score.strong.get_text()) #/score infomation

                    #print type(price.get_text())
                result=bsObj.h1.text+","+bsObj.h3.span.text+" ,"+bsObj.script.text +","+price.get_text()+","+score.strong.get_text()
                #print result.encode('utf-8')
                file.write(result.encode('utf-8')+"\n")
                print "write succ"
            except:
                continue

    except:
        continue
