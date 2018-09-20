import requests
from lxml import etree
import sys
from PIL import Image
import pytesseract
from urllib import parse
import re
import json
import execjs
import jsbeautifier

Lurl="https://sso.telnet404.com/cas/login?service=https%3A%2F%2Fwww.zoomeye.org%2Flogin"
Curl="https://sso.telnet404.com/captcha/"
headers = {
    'Host':'sso.telnet404.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
    'Referer':'https://www.zoomeye.org/login'
   
  }
iheaders = {
    'Host':'sso.telnet404.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
    'Referer':'https://sso.telnet404.com/cas/login?service=https%3A%2F%2Fwww.zoomeye.org%2Flogin'
   
  }
lheaders = {
    'Host':'sso.telnet404.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
    'Referer':'https://sso.telnet404.com/cas/login?service=https%3A%2F%2Fwww.zoomeye.org%2Flogin',
    'Content-Type':'application/x-www-form-urlencoded'

}
mheaders = {
    'Host':'www.zoomeye.org',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
    'DNT':"1"
}

zheaders = {
    'Host':'www.zoomeye.org',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
    'Accept':'application/json, text/plain, */*',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection':'keep-alive',
    'Accept-Encoding':'gzip, deflate, br',
    'DNT':"1",
    'Pragma':'no-cache',
    'Referer':'',
    'Cache-Control':'no-cache'
  }


data = {
    "csrfmiddlewaretoken":"",
    "email":"exinyijiu@163.com",
    "password":"a05370385a",
    "captcha":""
  }

while 1:
    s = requests.Session()
    out = s.get("https://sso.telnet404.com/cas/login?service=https%3A%2F%2Fwww.zoomeye.org%2Flogin",headers=headers)

    con = out.content.decode('utf-8')
    pp = etree.HTML(con)
    csrf = pp.xpath('//input[@name="csrfmiddlewaretoken"]/@value')

    im = s.get(Curl,headers=iheaders)

    with open("ze.img","wb") as f:
        f.write(im.content)
    cc = Image.open("ze.img")
    pytes = pytesseract.image_to_string(cc)

    data['csrfmiddlewaretoken'] = csrf[0].strip()
    data['captcha'] = pytes
    vvv = s.post(Lurl,headers=lheaders,data=data,allow_redirects=True)

    if "请输入正确的验证码" in vvv.content.decode("utf-8"):
        continue
    else:
       
        ddd = parse.urlparse(vvv.url)       
        zheaders['Referer'] = vvv.url
        pro = s.get("https://www.zoomeye.org/user/login?{}".format(ddd.query),headers=zheaders)
        hi = ''.join(re.findall('<script>(.*?)</script>',pro.text))
       
     
        by = execjs.compile(hi.replace('eval(','return('))
        hello = by.call(f)
        if not hello.startswith('var'):
            print("非var开头")
            continue
        sss = re.match(r'var (.*?)=',hello).group(1)

        
        hhello = hello.replace('document.cookie=','return').replace(';if((function(){try{return !!window.addEventListener;}','').\
        replace("catch(e){return false;}})()){document.addEventListener('DOMContentLoaded',%s,false)}" % sss,'').\
replace("else{document.attachEvent('onreadystatechange',%s)}" % sss,'').replace(r"setTimeout('location.href=location.pathname+location.search.replace(/[\?|&]captcha-challenge/,\'\')',1500);",'').replace('window','')
       

        conte = execjs.compile(hhello)
        try:
            jsclear = conte.call('%s' % sss)
        except Exception as e:
        
            continue
        uidc = requests.utils.dict_from_cookiejar(pro.cookies)
        uidcookie = ''.join([f + "=" + v for f,v in uidc.items()])
        #jsclearcook = parse.unquote(jsclear.split(';')[0])
        jsclearcook = jsclear.split(';')[0]
        print(jsclearcook)
        mheaders['Cookie'] = uidcookie + ";" + jsclearcook
        mheaders['Referer'] = "https://www.zoomeye.org/login?{}".format(ddd.query)
        print(mheaders)
        hhhh = s.get("https://www.zoomeye.org/user/login?{}".format(ddd.query),headers=mheaders)
        print(hhhh.text)
        break
