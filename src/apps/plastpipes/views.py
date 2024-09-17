from django.shortcuts import render
from rest_framework import generics

from . import models, serializers

# Create your views here.


class PlastPipesCategoryListAPIView(generics.ListAPIView):
    queryset = models.PlastPipesCategory.objects.all()
    serializer_class = serializers.PlastPipesCategorySerializer
