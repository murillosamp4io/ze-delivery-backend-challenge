from django.contrib.gis.db import models as gis_db
from django.db import models


class Partner(models.Model):
    tradingName = models.CharField(max_length=150, blank=False)
    ownerName = models.CharField(max_length=100, blank=False)
    document = models.CharField(max_length=18, blank=False, default='', unique=True)
    coverageArea = gis_db.MultiPolygonField(blank=True)
    address = gis_db.PointField(blank=False)

    def __str__(self):
        return self.tradingName
