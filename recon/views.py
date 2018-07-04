from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

import re

####### func ######



# Create your views here.
####### view ######

def index(request):
    if request.method == 'POST':
        print(request.POST.get('keyword'))
        print(request.POST.get('seatype'))
    return render(request,"search.html")



