from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import List_of_Alerts,Log_of_all_sent_alerts
from .serializers import List_of_AlertsSerializer,Log_of_all_sent_alertsSerializer

class List_of_AlertsView(ListAPIView):
    queryset=List_of_Alerts.objects.all()
    serializer_class=List_of_AlertsSerializer

class Log_of_all_sent_alertsView(ListAPIView):
    queryset=Log_of_all_sent_alerts.objects.all()
    serializer_class=Log_of_all_sent_alertsSerializer
