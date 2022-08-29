from ast import Str
from email import message
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
from django.shortcuts import redirect, render,HttpResponseRedirect
import urllib.parse
urllib.parse.quote(':')
'%3A'
import random
from django.contrib import messages
#from django.core.exceptions import ObjectDoesNotExist

 

# Create your views here.

    
def home(request):
    
    return render(request,'home.html',{'name':'home.html'})

def POST(request):
    global val
    val=request.POST.get('Rollno')
    try:
        z = Result1.objects.get(pk=val)
        print("========",z)
        print("========",val)
        
        return render(request,'result2.html',{'result': z})
    except:
        message='Entered Rollno '+str(val) +' does not exist in DB'
        return render(request,'home.html',{"message":message})
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
        DebuggingServer
        # y = request.POST.get("demo")
        y = request.POST.get("data1")
        x = val
        l = request.POST.get("imgFinger1")
        r = request.POST.get("imgFingerrti1")
        t = request.POST.get("txtIsoImage")
        p = request.POST.get("txtIsoImagerti")
        number1 = random.randint(1000,9999)
        number2 = str(number1)
        print(number1)
        if Result1.objects.filter(bib_r1=Result1.bib_r1).exists():
            message='bibno is already exist'
            
            return HttpResponse(message)
        else:
            if dtf.chipno_1_R1==dtf.chipno_1_R2:
                        message='entered values of chipno 1 and chipno 2 is same'
                        return HttpResponse(message)
            
            else:
                if Result1.objects.filter(chipno_1_R1=Result1.chipno_1_R1).exists():
                    message='chipno 1 is already exist'
                    return HttpResponse(message)
                
                else:
                    if Result1.objects.filter(chipno_1_R2=Result1.chipno_1_R2).exists():
                        message='chipno 2 is already exist'
                        return HttpResponse(message)
                    else:
                        if Result1.objects.filter(chipno_1_R2=Result1.chipno_1_R1).exists():
                            message='entered chipno 1 is already exist in chipno 2 in DB'
                            return HttpResponse(message)
                        else:
                            if Result1.objects.filter(chipno_1_R1=Result1.chipno_1_R2).exists():
                                message='entered chipno 2 is already exist in chipno 1 in DB '
                                return HttpResponse(message)
                            else:
                                dtf.save()
                                img = Imagedata(rollno=x, imagedata=y,ltiimagedata=l,rtiimagedata=r,lti_iso=t,rti_iso=p,number=number1)
                                img.save()
                                
                                return HttpResponse(str(val) +' unique id is '+ str(number1))                           










#return redirect('result2.html')
                
            #return render(request, 'result2.html',{"message":'unique id is ' + number2})
            
            
            #render(request, 'result2.html',{"message":"Candidate registered "} )
         
                                        #return render(request, 'result2.html',{"message":"Candidate updated successfully"})
