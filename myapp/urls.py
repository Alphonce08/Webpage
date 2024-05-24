from django.urls import path
from . import views


app_name = "myapp"
urlpatterns = [
    path('', views.index, name='index'),
    path('soft', views.soft, name='soft'),
    path('team', views.team, name='team'),
    path('fash', views.fash, name='fash'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('classes', views.classes, name='classes'),
    path('hover', views.hover, name='hover'),
    path('dynamic', views.dynamic, name='dynamic'),
    path('contact', views.contact, name='contact')
    ]