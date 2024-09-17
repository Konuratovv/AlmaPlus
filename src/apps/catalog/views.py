from django.shortcuts import render
from rest_framework import generics

from . import models
from . import serializers

# Create your views here.


class CatalogListAPIView(generics.ListAPIView): 
    queryset = models.Catalog.objects.all()
    serializer_class = serializers.CatalogSerializer