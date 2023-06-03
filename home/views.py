from django.http import HttpRequest
from django.shortcuts import render

def home(request:HttpRequest):
    return render(request,'main.html')



def header_component(request:HttpRequest):
    context = {}
    return render(request,'layout/header_component.html',context)


def footer_component(request:HttpRequest):
    context = {}
    return render(request,'layout/footer_component.html',context)