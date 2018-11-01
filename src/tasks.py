from __future__ import absolute_import,unicode_literals
from celery import shared_task
from .models import asset
from telnetlib import Telnet
import sys

def telver(ip,port):
    try:
        Telnet(ip,port,timeout=6)
        return True
    except Exception as e:
        return False


@shared_task
def verurl():
    url = asset.objects.all()[1:3]
    c = (i for i in url)
    for d in c:
        print(d.ip)
       
