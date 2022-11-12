from django.shortcuts import render
from rest_framework import generics
from . models import User
from .serializers import *
# Create your views here.

class ItemList(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
    

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
