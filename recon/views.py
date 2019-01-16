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
from utils.tools import Ctools
from utils.crawler.bddock import bdsou
from django.views.decorators.csrf import csrf_exempt

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
        stat = request.POST.get('status')
        print(stat)
        sdata = {'status':0,'data':''}
        hello = Ctools()
        print(udomain)
        if type == "1":
            sdata['data'] = ''
            doda = hello.domain(udomain,Surl,Sudata) 
            sdata['data'] = doda
        elif type == "2":
            sdata['data'] = ''
            ddoda = hello.dodir(udomain)
            sdata['data'] = ddoda 
        print(sdata)
        sd = json.dumps(sdata)
        return HttpResponse(sd)     
@login_required()
@csrf_exempt
def dsou(request):     
    if request.method == "POST":
        ddata = {'status':0,'data':''}
        dtype = request.POST.get('seatype')
        dudomain = request.POST.get('keyword')
        print(dtype)
        if dtype == "1":
            v = bdsou(dudomain)
            ddata['data'] = v
        dd = json.dumps(ddata)
        return HttpResponse(dd,content_type="application/json") 
    return render_to_response("dsou.html")


