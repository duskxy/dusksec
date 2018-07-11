from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

import re
import sublist3r
import subprocess

####### func ######



# Create your views here.
####### view ######
tools = "/data/py/sec/dusksec/utils"

def login(request):
    return render(request,"login.html")


def index(request):
    idtext = ""
    ic = ""
    if request.method == 'POST':
        ky = request.POST.get('keyword')
        ty = request.POST.get('seatype')
        if ty == "1":
            p = subprocess.Popen(tools+"/Sublist3r/sublist3r.py -d {}".format(ky),stdout=subprocess.PIPE,shell=True)
            idtext = p.stdout.read().strip()
            ic = re.findall("[0-9a-z]{5}\."+ky,str(idtext))
            print(ic[0])
    return render(request,"search.html",{"dotext":ic})



