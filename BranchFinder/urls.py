from django.urls import path
from . import views

urlpatterns = [
    path('', views.BranchFinder, name='BranchFinder'),
    #path('password', views.PassView, name='Password'),
]