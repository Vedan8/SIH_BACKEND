from rest_framework import serializers
from .models import Vessels

class VesselSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vessels
        fields="__all__"

