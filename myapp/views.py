from django.shortcuts import render,redirect
from . import views
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'index.html')

def fash(request):
    return render(request, 'fash.html')

def soft(request):
    return render(request, 'soft.html')