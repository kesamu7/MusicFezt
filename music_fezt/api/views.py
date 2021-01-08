# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics, status
from django.shortcuts import render
from .serializers import RoomSerializer, CreateRoomSerializer
from .models import Room
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
