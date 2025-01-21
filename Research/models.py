from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class Location(models.Model):
    name = models.CharField(max_length=100)
    #point = models.PointField()
    geom = models.GeometryField(default=Point(0.0,0.0))

    def __str__(self):
        return self.name

