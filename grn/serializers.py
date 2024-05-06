from rest_framework import serializers
from .models import Grn, GrnDetail


class GrnDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrnDetail
        fields = '__all__'

class GrnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grn
        fields = '__all__'

