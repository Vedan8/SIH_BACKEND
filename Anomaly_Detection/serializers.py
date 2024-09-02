from rest_framework import serializers
from .models import Recent_Ship_Issues,Anomaly_Detail

class Recent_Ship_IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recent_Ship_Issues
        fields="__all__"

class Anomaly_DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Anomaly_Detail
        fields="__all__"