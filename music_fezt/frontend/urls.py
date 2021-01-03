from django.conf.urls import url
from .views import index
from django.urls import path

urlpatterns = [
    
    path('',index)
]