from rest_framework import serializers

from . import models


class AboutUsMainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutUsMainPage
        fields = ('image', 'description')


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutUs
        fields = (
            'title',
            'description',
        )