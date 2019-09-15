from django.db import models
import math
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

    def get_si_distance(self, p):
        lat1 = self.latitude
        lon1 = self.longitude
        lat2 = p[0]
        lon2 = p[1]
        R = 6378.137  # Radius of earth in KM
        dLat = lat2 * math.pi / 180 - lat1 * math.pi / 180
        dLon = lon2 * math.pi / 180 - lon1 * math.pi / 180
        a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(lat1 * math.pi / 180) * math.cos(lat2 * math.pi / 180) * math.sin(dLon / 2) * math.sin(dLon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = R * c
        return d * 1000  # meters


class PointUser(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    time = models.DateTimeField()


# class PointVisit(models.Model):
#     point_of_interest = models.ForeignKey(PointOfInterest, on_delete=models.DO_NOTHING)
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()

#     def __str__(self):
#         print(type(self.start_time))
#         return self.point_of_interest.name + '[' + str(self.end_time - self.start_time) + ']'
