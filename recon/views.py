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
tools = "/data/py/dusksec"

def login(request):
    return render(request,"login.html")


def index(request):
    idtext = ""
    ic = ""
    icq = ""
    if request.method == 'POST':
        ky = request.POST.get('keyword')
        ty = request.POST.get('seatype')
        if ty == "1":
            p = subprocess.Popen(tools+"/utils/Sublist3r/sublist3r.py -d {} -o"+ tools+"common/{}.txt".format(ky,ky),stdout=subprocess.PIPE,shell=True)
            out,err = p.communicate()
            if p.returncode != 0:
                pass
                    
    return render(request,"search.html")

def domain(request):
    if request.method == "POST":
        print(request.POST)
