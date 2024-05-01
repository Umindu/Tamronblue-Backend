from rest_framework import serializers
from .models import LandPlant

class LandPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandPlant
        fields = '__all__'
