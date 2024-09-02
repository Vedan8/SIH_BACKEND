from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Recent_Ship_Issues,Anomaly_Detail
from .serializers import Recent_Ship_IssueSerializer,Anomaly_DetailSerializer

class Recent_Ship_IssuesView(ListAPIView):
    serializer_class=Recent_Ship_IssueSerializer
    queryset=Recent_Ship_Issues.objects.all()

class Anomaly_DetailView(ListAPIView):
    serializer_class=Anomaly_DetailSerializer
    queryset=Anomaly_Detail.objects.all()