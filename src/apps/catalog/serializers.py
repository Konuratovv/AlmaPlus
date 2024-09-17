from rest_framework import serializers

from . import models


class CatalogSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Catalog  
        fields = (
            'image',
            'title',
            'description',
        )