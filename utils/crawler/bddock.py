import requests
from lxml import etree
from urllib import parse
import re
import sys

headers = {
    "Host":"www.baidu.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
    "Referer":"https://www.baidu.com/"

}
comp = re.compile(r"(http|https)://\w+?\.\w+(\.\w+){0,5}")
def bdsou(url):
    bdurl = "https://www.baidu.com/s?wd={}&pn={}"
    print(bdurl + parse.quote(url))
    urlen = parse.quote(url)
    rrl = set()
    for np in range(0,10000,10):
        ret = requests.get(bdurl.format(urlen,np),headers=headers,timeout=5)
        hx = ret.content.decode("utf-8",'ignore')
        jx = etree.HTML(hx)
        reurl = jx.xpath('//a[@class="c-showurl"]/text()')
        for i in reurl:
            if 'baidu.com' in i or len(i) < 5:
                pass
            elif i.startswith("http") or i.startswith("https"):
                ppp = comp.match(str(i))
                if ppp:
                    #print(ppp.group())
                    rrl.add(ppp.group())
            else:
                clppp = "http://" + i
                clvvv = comp.match(clppp)
                if clvvv:
                    rrl.add(clvvv.group())
    return list(rrl)
