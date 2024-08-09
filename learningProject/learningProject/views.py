from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("hello, world. Home Page")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("hello, world. About Page")

def contact(request):
    return HttpResponse("hello, world. Contact Page")

