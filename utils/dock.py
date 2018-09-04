import requests
from lxml import etree
from urllib import parse

headers = {
    "Host":"www.baidu.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
    "Referer":"https://www.baidu.com/"

}


bdurl = "https://www.baidu.com/s?wd="
url = input("请输入dork:")
print(bdurl + parse.quote(url))
urlen = parse.quote(url)
re = requests.get(bdurl+urlen,headers=headers)
hx = re.content.decode("utf-8")
jx = etree.HTML(hx)
reurl = jx.xpath('//a[@class="c-showurl"]/text()')
for i in reurl:
    print(i)
