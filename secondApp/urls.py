from django.urls import path
from secondApp import views

urlpatterns = [
    path('', views.home, name='homepage')
]