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
def about(request):
    return render(request, 'about.html')
def team(request):
    return render(request, 'team.html')
def blog(request):
    return render(request, 'blog.html')
def classes(request):
    return render(request, 'classes.html')
def hover(request):
    return render(request, 'hover.html')
def dynamic(request):
    return render(request, 'dynamic.html')

def contact(request):
    return render(request, 'contact.html')