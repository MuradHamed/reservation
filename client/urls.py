from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('index', views.index),
    path('header', views.header),
    path('info', views.info),
    path('addproduct', views.addproduct),
    path('addclient', views.add_client),
    path('clientlist', views.client_list),


]



