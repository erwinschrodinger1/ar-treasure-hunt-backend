from rest_framework import serializers
from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['latitude', 'longitude', 'user']
        model = Location
