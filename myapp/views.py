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


<<<<<<< HEAD
def classes(request):
    return render(request, 'classes.html')



def blog(request):
    return render(request, 'blog.html')


def sale(request):
    return render(request, 'sale.html')
=======
def team(request):
    return render(request, 'team.html')

def blog(request):
    return render(request, 'blog.html')
>>>>>>> af6514201eb3e25aeadbdd1ca280b23217cb423a
