from django.db import models

class Recent_Ship_Issues(models.Model):
    time=models.DateTimeField()
    departed_from=models.CharField(max_length=50)
    speed=models.CharField(max_length=10)

class Anomaly_Detail(models.Model):
    anomaly_type=models.CharField(max_length=50)
    severity=models.CharField(max_length=10)
    latitude=models.CharField(max_length=20)
    longitude=models.CharField(max_length=20)
    name=models.CharField(max_length=50)
    mmsi=models.CharField(max_length=50)
    date_time=models.DateTimeField()