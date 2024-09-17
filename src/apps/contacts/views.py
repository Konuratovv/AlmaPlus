from django.shortcuts import render

from rest_framework.generics import ListAPIView

from . import models, serializers

# Create your views here.


class ContactsListAPIView(ListAPIView):
    queryset = models.Contacts.objects.all()
    serializer_class = serializers.ContactsSerializer
