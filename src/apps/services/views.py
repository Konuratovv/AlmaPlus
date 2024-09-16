from django.shortcuts import render
from rest_framework import generics
from . import serializers
from . import models

# Create your views here.


class ServicesListAPIView(generics.ListAPIView):
    serializer_class = serializers.ServiceSerializer
    queryset = models.Service.objects.all()