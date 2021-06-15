from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    return HttpResponse("<h1 style='color:red;text-align:center'>home page app3</h1>")

def product(request):
    
    return HttpResponse("<h1 style='color:red;text-align:center'>product page app3</h1>")

def customer(request):
    
    return HttpResponse("<h1 style='color:red;text-align:center'>customer page app3</h1>")