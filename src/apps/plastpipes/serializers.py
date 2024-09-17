from rest_framework import serializers
from . import models


class PlastPipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlastPipe
        fields = (
            'image',
            'description'
        )


class PlastPipesCategorySerializer(serializers.ModelSerializer):
    plast_pipes = serializers.SerializerMethodField()

    class Meta:
        model = models.PlastPipesCategory
        fields = (
            'title',
            'plast_pipes',
        )

    def get_plast_pipes(self, obj):
        return PlastPipesSerializer(obj.pipes.filter(id=obj.id), many=True).data