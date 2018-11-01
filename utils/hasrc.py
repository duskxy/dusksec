import requests
from lxml import etree
import sys
from urllib import parse
import asyncio
from pyppeteer.launcher import launch

async def main(url):
    brower = await launch({'headless': True,'args':['--no-sandbox'],})
    page = await brower.newPage()
    await page.setUserAgent('Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0')
    resu = await page.goto(url)
    retex = await resu.text()
    print(retex)




url = 'https://hackerone.com/directory?query=' + parse.quote('bounties%3Ayes&sort=published_at%3Adescending&page=1')
headers = {
   'Host':'hackerone.com',
   'User-Agent':'user-agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
   'Cookie':'_ga=GA1.2.371582329.1537710765; _mkto_trk=id:168-NAU-732&token:_mch-hackerone.com-1537710764766-21110; _biz_uid=46dd042bb3b94da6de44a240200ed375; _biz_nA=6; _biz_pendingA=%5B%5D; _biz_flagsA=%7B%22Version%22%3A1%2C%22Mkto%22%3A%221%22%2C%22XDomain%22%3A%221%22%7D; __cfduid=d337a7571bf907c59d4425ae926f61a011537710525; _cfuid=c8dff823-508b-40cd-b618-e89fa88860f2; __Host-session=UmZ4V0xHK0NpcUkwT1FZZ2lJaG9RdzVreERhSXIwZWF6c29PRDR6Rmc0cmFFdEFBTzhESnltQUFrcjhlQ3M2bmdZZ3hRbWFEQVFVTjlHRjZrZEZJTDFHS3BHL3BlYy9MOWpzU0tKdk1sSEU5bXFCNXZVY3NaNWw5WW8xSE1sWVMvSmg5aTdTQ1EzMmVmUGJWamZwV2dnPT0tLTlrUTJEeUg0L1dZS1F2Nk1DTmRVRFE9PQ%3D%3D--82a6a1f1f34a268fddb2c06371410015a6e2bc20; _gid=GA1.2.1703458676.1540985307; _gat=1'
   }

#for i in range(1,5):
#    result = requests.get(url.format(i),headers=headers)
#    print(result.content)
#    sys.exit()
eloop = asyncio.get_event_loop()
eloop.run_until_complete(main(url))
