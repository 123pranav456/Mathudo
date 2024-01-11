import math as m
import decimal as d
from django.shortcuts import render
from .models import sticker
# Create your views here.
def home(request):

    return render(request,'page1.html')

def index(request):
    return render(request,'page2.html')

def add(request):
   
    val1= int(request.POST['first'])
    val2=int(request.POST['second'])
    a=request.POST['operation']
    if  a=='Addition':
       res=val1+val2
    elif a=='Subtraction':
        if val1>val2:
          res=val1-val2
        elif val2>val1:
            res=val2-val1  
    elif a=='Multiplication' :
            res=-val1*val2  
            if res<0:
                res=-1*(res)  
    elif a=='Division':
     res=val1//val2 
      
    return render(request,'page2.html',{'result':res})

def p3(request):
   
        
    return render(request,'page3.html')

def trigo(request):
    val= int(request.POST['first'])
    c=(request.POST['type'])
    b=(request.POST['operation'])
    if c=='degrees':
        if b=='sin':
          x=m.sin(m.radians(val))
          res=round(x,2)
        elif b=='cos':
          x=m.cos(m.radians(val))
          res=round(x,2)
    elif c=='radians':
        if b=='sin':
          x=m.sin(m.degrees(val))
          res=round(x,2)
        elif b=='cos':
          x=m.cos(m.degrees(val))
          res=round(x,2)
        
    return render(request,'page3.html',{'result':res})