from django.urls import path
from . import views


app_name = "myapp"

urlpatterns = [

    path('', views.index, name='index'),
    path('fash', views.fash, name='fash'),
    path('soft', views.soft,  name='soft'),
<<<<<<< HEAD
    path('about', views.about,  name='about'),
    path('blog', views.blog,  name='blog'),
    path('classes', views.classes,  name='classes'),
    path('sale', views.sale,  name='sale')
=======
    path('team', views.team,  name='team'),
    path('about', views.about,  name='about'),
    path('blog', views.blog,  name='blog')
>>>>>>> af6514201eb3e25aeadbdd1ca280b23217cb423a
    ]