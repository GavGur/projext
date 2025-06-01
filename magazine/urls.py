from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('index2', views.index, name="home"),
    path('stest', views.test, name="catalog"),
    path('index', views.register, name="register"),
    path('index3', views.vhod, name="vhod"),
    path('test', views.test_second, name="test")
]
