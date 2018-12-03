from django.shortcuts import render,render_to_response
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from dwebsocket.decorators import accept_websocket,require_websocket
from .models import Surl,Sudata

import re
import sublist3r
import subprocess
import json

####### func ######



# Create your views here.
####### view ######
tools = "/data/py/dusksec"

def login(request):
    if request.mothed == 'GET':
        return render(request,"login.html")
    elif request.methed == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')


@login_required()
def index(request):
    return render(request,"search.html")
@login_required()
def domain(request):
    if request.method == "POST":
        type = request.POST.get("seatype")
        udomain = request.POST.get("keyword")
        sdata = {'status':0,'data':[]}
        if type == "1":
            result = subprocess.Popen(tools + "/utils/Sublist3r/sublist3r.py -d {} ".format(udomain) + "-o " + tools + "/common/{}.txt".format(udomain),stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
            while 1:
                out = result.stdout.readline().decode("utf-8")
                if out == '':
                    su = Surl(url=udomain)
                    su.save()
                    with open(tools + "/common/{}.txt".format(udomain),"r") as ff:
                        for i in ff.readlines():
                            ii = i.strip()
                            sd = Sudata(url=ii,uid_id=su.id)
                            sd.save()
                            sdata["data"].append(ii)
                    break 
                print(out.strip())
        sd = json.dumps(sdata)
        return HttpResponse(sd)     
@login_required()
def dnslog(request):
    return render_to_response("dnslog.html")
