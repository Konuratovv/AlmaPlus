from django.shortcuts import render

from rest_framework import generics

from . import models, serializers

# Create your views here.


class AboutUsMainPageAPIVIew(generics.ListAPIView):
    queryset = models.AboutUsMainPage.objects.all()
    serializer_class = serializers.AboutUsMainPageSerializer


class AboutUsAPIView(generics.ListAPIView):
    queryset = models.AboutUs.objects.all()
    serializer_class = serializers.AboutUsSerializer
