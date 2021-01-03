# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from django.shortcuts import render
from .serializers import RoomSerializer
from .models import Room

# Create your views here.
class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
