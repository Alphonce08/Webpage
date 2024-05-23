from django.urls import path
from . import views


app_name = "myapp"

urlpatterns = [
    
    path('', views.index, name='index'),
    path('fash', views.fash, name='fash'),
    path('soft', views.soft,  name='soft')
    ]