import requests
import os,sys
import django
sys.path.append('/data/py/dusksec')
os.environ['DJANGO_SETTINGS_MODULE'] = 'dusksec.settings'
django.setup()
from src.models import Src
from lxml import etree


smast = "https://www.anquanke.com"

src = "https://www.anquanke.com/src"

def resrc():
    result = requests.get(src).content.decode("utf-8")
    v = etree.HTML(result)
    link = v.xpath('//div[@class="src-list"]//a/@href')
    urllist = []
    for i in link:
        result1 = requests.get(smast + i).content.decode("utf-8")
        u = etree.HTML(result1)
        link1 = ''.join(u.xpath('//div[@class="src-banner-cover"]/h3/text()'))
        urlsafe = ''.join(u.xpath('//div[@class="src-detail-content"]/div[2]/h3/a/@href'))
        yield link1,urlsafe
for x,y in resrc():
    print("{}-{}".format(x,y))
    p = Src.objects.filter(company=x).first()
    if not p:
        smod = Src(company=x,url=y)
        smod.save()   
