from django.db import models
import numpy

# Create your models here.


class PointOfInterest(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name + '[lat:' + str(self.latitude) + ', long:' + str(self.longitude) + ']'

    def get_point(self):
        return numpy.array([self.latitude, self.longitude])

    def get_distance(self, point):
        return numpy.linalg.norm(point - self.get_point())


class PointVisit(models.Model):
    point_of_interest = models.ForeignKey(PointOfInterest, on_delete=models.DO_NOTHING)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        print(type(self.start_time))
        return self.point_of_interest.name + '[' + str(self.end_time - self.start_time) + ']'
