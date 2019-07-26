# chat/urls.py
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('smallDisplay/', views.smallDisplay, name='smallDisplay'),
    path('largeDisplay/', views.largeDisplay, name='largeDisplay'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]

