from django.shortcuts import render
from rest_framework import generics


# Create your views here.
def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')


