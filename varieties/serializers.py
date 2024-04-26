from rest_framework import serializers
from .models import Variety

class VarietySerializer(serializers.ModelSerializer):
    class Meta:
        model = Variety
        fields = ['name', 'description', 'plant_id', 'status', 'created_at', 'updated_at']