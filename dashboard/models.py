from django.db import models

class Vessels(models.Model):
    MMSI=models.CharField(max_length=50)
    TIME=models.DateTimeField()
    LONGITUDE=models.CharField(max_length=50)
    LATITUDE=models.CharField(max_length=50)
    COG=models.CharField(max_length=50)
    SOG=models.CharField(max_length=50)
    HEADING=models.CharField(max_length=50)
    ROT=models.CharField(max_length=50)
    NAVSTAT=models.CharField(max_length=50)
    IMO=models.CharField(max_length=50)
    NAME=models.CharField(max_length=50)
    CALLSIGN=models.CharField(max_length=50)
    TYPE=models.CharField(max_length=50)
    A=models.CharField(max_length=50)
    B=models.CharField(max_length=50)
    C=models.CharField(max_length=50)
    D=models.CharField(max_length=50)
    DRAUGHT=models.CharField(max_length=50)
    DEST=models.CharField(max_length=50)
    ETA=models.TimeField()

