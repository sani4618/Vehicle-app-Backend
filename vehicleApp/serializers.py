from rest_framework import serializers
from vehicleApp.models import VehicleAppModel


class VehicleAppSerializer(serializers.ModelSerializer):
    class Meta:
        model=VehicleAppModel
        fields=(

           'vehiclenum',
            'model',
            'brand',
            'manfyear',
            'color',
            'ownername',
            'address',
            'phNum',
            'image'
        )