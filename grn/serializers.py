from rest_framework import serializers
from .models import Grn, GrnDetail

class GrnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grn
        fields = '__all__'

class GrnDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrnDetail
        fields = '__all__'
