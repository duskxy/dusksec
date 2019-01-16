import requests
import aiohttp
import asyncio
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
semp = asyncio.Semaphore(10)
#for np in range(0,1000000,10):
async def febd(urllen,page):
    with (await semp):
        async with aiohttp.ClientSession() as session:
            async with session.get(bdurl.format(urllen,page),headers=headers,timeout=60) as s:
                #await hx = s.content.decode("utf-8",'ignore')
                hx = await s.text()
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
if __name__ == "__main__":
    bdurl = "https://www.baidu.com/s?wd={}&pn={}"
    url = input("请输入dork:")
    print(bdurl + parse.quote(url))
    urlen = parse.quote(url)
    rrl = set()
    loopup = asyncio.get_event_loop()
    tasks = [febd(urlen,i) for i in range(0,1000000,10)]
    loopup.run_until_complete(asyncio.gather(*tasks))
    print("***{}".format(len(rrl)))
    for i in rrl:
        print(i)
