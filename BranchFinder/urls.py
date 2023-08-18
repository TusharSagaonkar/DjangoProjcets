from django.urls import path
from . import views

urlpatterns = [
    path('BrFind', views.BranchFinder, name='BranchFinder'),
    path('', views.Home, name='Home'),
    path('home', views.Home, name='Home'),
    path('RRN', views.RRN, name='RRN'),   
    path('rrn', views.RRN, name='rrn'),
    path('link', views.link_list, name='Link'),
]