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
#实现遍历页面爬虫，提取中关村手机信息,标题\上市时间\URL\提取价格信息\评分,共5个元素。把要提取的5个信息放在同一行输入，且逗号分隔。


