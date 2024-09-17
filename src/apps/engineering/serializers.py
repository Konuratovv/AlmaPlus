from rest_framework import serializers

from . import models

class EngineeringSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Engineering
        fields = ('title', 'description')


class EngineeringCategorySerializer(serializers.ModelSerializer):
    engineering = serializers.SerializerMethodField()


    class Meta:
        model = models.EngineeringCategory
        fields = ('title', 'engineering')

    def get_engineering(self, obj):
        return EngineeringSerializer(obj.engineering.filter(id=obj.id), many=True).data