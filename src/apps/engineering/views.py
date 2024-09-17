from django.shortcuts import render

from rest_framework import generics

from . import models, serializers

# Create your views here.

class EngineeringAPIView(generics.ListAPIView):
    queryset = models.EngineeringCategory.objects.all()
    serializer_class = serializers.EngineeringCategorySerializer  