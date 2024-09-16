from rest_framework import serializers
from .models import ServiceCategory, Service


class CategoryServiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ServiceCategory
        fields = ('id', 'title', )


class ServiceSerializer(serializers.ModelSerializer):
    category = CategoryServiceSerializer()

    class Meta:
        model = Service
        fields = ('id', 'text', 'category', )