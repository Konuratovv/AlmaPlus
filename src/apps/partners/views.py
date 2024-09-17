from django.shortcuts import render

from rest_framework import generics

from . import models, serializers

# Create your views here.


class PartnersListAPIView(generics.ListAPIView):
    queryset = models.Partner.objects.all()
    serializer_class = serializers.PartnerSerializer

