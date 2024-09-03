from rest_framework import serializers
from .models import List_of_Alerts,Log_of_all_sent_alerts

class List_of_AlertsSerializer(serializers.ModelSerializer):
    class Meta:
        model=List_of_Alerts
        fields="__all__"

class Log_of_all_sent_alertsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Log_of_all_sent_alerts
        fields="__all__"