import datetime

from django.db                  import models

# Create your models here.


class City(models.Model):
    city_name               = models.CharField(max_length=200)
    city_code               = models.CharField(max_length=4)
    geo_latitude            = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    geo_longitude           = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    country                 = models.ForeignKey('country.Country', on_delete=models.PROTECT, related_name='citys')

    def __str__(self):
        return self.city_name
