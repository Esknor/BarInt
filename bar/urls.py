from django.contrib import admin
from django.conf.urls import include, url
from bar import views




urlpatterns = [
 url(r'^$', views.home, name='home'),
 url(r'^$', views.home_page, name='home_page'),
 url(r'^$', views.tren_page, name='tren'),
]