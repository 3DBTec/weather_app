import datetime

from django.db                  import models

# Create your models here.


class Country(models.Model):

    CONTINENTS = (
        ('AF', 'Africa'),
        ('AS', 'Asia'),
        ('AN', 'Antartica'),
        ('EU', 'Europe'),
        ('NA', 'North America'),
        ('SA', 'South America')
    )

    country_name          = models.CharField(max_length=200)
    country_code          = models.CharField(max_length=3)
    continent             = models.CharField(choices=CONTINENTS, default='AF', max_length=30)

    def __str__(self):
        return self.country_name
