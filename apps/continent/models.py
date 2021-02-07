import datetime

from django.db                  import models

# Create your models here.


class Continent(models.Model):
    continent_name          = models.CharField(max_length=200)
    continent_code          = models.CharField(max_length=2)

    def __str__(self):
        return self.continent_name
