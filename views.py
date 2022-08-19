from ast import Str
from smtpd import DebuggingServer
from sre_constants import SUCCESS
from tokenize import Name
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Result1,Imagedata,uuid
from django.urls import reverse
from os import path
from tkinter import Image
from urllib.request import urlopen
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.shortcuts import redirect, render
import urllib.parse
urllib.parse.quote(':')
'%3A'
import random

 

# Create your views here.

    
def home(request):
    
    return render(request,'home.html',{'name':'home.html'})

def POST(request):
    global val
    val=request.POST.get('Rollno')
    z = Result1.objects.get(pk=val)
    print("========",z)
    print("========",val)
    
    return render(request,'result2.html',{'result': z})

def add1(request):
                    
    if request.method == 'POST':
        Result1.bib_r1=request.POST.get('bibno')
        print("bib======",Result1.bib_r1)
        Result1.chipno_1_R1=request.POST.get('chip1')
        print("chip1======",Result1.chipno_1_R1)
        Result1.chipno_1_R2=request.POST.get('chip2')
        print("chip2======",Result1.chipno_1_R2)
        
    
        
        
        dtf=Result1.objects.get(pk=val)
        print("========",dtf)
        dtf.bib_r1=Result1.bib_r1
        dtf.chipno_1_R1=Result1.chipno_1_R1
        dtf.chipno_1_R2=Result1.chipno_1_R2
        dtf.save()
        
        
        DebuggingServer
        # y = request.POST.get("demo")
        y = request.POST.get("data1")
        x = val
        l = request.POST.get("imgFinger1")
        r = request.POST.get("imgFingerrti1")
        t = request.POST.get("txtIsoImage")
        p = request.POST.get("txtIsoImagerti")
        number1 = random.randint(1000,9999)
        print(number1)
        img = Imagedata(rollno=x, imagedata=y,ltiimagedata=l,rtiimagedata=r,lti_iso=t,rti_iso=p,number=number1)
        img.save()

        return HttpResponse(number1)                           #render(request, 'result2.html',{"message":"Candidate registered "} )
    
#def image_upload(request):
   # return HttpResponse(success)                                          #return render(request, 'result2.html',{"message":"Candidate updated successfully"})

