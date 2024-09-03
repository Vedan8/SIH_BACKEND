from django.db import models

class List_of_Alerts(models.Model):
    date=models.DateField()
    type=models.CharField(max_length=50)
    severity=models.CharField(max_length=20)

class Log_of_all_sent_alerts(models.Model):
    date=models.DateField()
    time=models.TimeField()
    type=models.CharField(max_length=50)
    sent_to=models.CharField(max_length=50)
