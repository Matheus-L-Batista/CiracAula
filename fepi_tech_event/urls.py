from django.contrib import admin
from django.urls import path, include
from fepi_tech_event.views import index 


urlpatterns = [
    path('index/',index),
    
]