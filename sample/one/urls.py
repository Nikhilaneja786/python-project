from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('one/', views.first,name='one/'),
    path('',views.hfirst)
]