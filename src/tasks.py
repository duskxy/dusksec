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
    url = asset.objects.all()
    c = (i for i in url)
    for d in c:
        v = d.ip.split(':')
        if telver(v[0],v[1]) is False:
            asset.objects.filter(ip=d.ip).update(status='2')
