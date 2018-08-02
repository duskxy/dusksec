from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from dwebsocket.decorators import accept_websocket,require_websocket

import re
import sublist3r
import subprocess

####### func ######



# Create your views here.
####### view ######
tools = "/data/py/sec/dusksec/utils"

def login(request):
    return render(request,"login.html")

@accept_websocket
def index(request):
    if not request.is_websocket():
        return render(request,'search.html')
    else:
        #ky = request.POST.get('keyword')
        #ty = request.POST.get('seatype')
        ty = request.websocket.read()
        if ty == "1":
            p = subprocess.Popen(tools+"/Sublist3r/sublist3r.py -d {}".format(ky),stdout=subprocess.PIPE,shell=True)
            idtext = p.stdout.read().strip()
            ic = re.findall("[0-9a-z]{5}\."+ky,str(idtext))
            icq = "\r\n".join(ic)
            print(ic[0])
    return render(request,"search.html",{"dotext":icq})



