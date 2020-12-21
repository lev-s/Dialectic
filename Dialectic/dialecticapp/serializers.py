from rest_framework import serializers
from .models import dialecticapp

class dialecticappSerializer(serializers.ModelSerializer):
    class Meta:
        model = dialecticapp
        fields = ('__all__')