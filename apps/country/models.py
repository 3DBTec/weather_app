import datetime

from django.db                  import models

# Create your models here.


class Country(models.Model):

    # CONTINENTS = (
    #     ('available', _('Available to borrow')),
    #     ('borrowed', _('Borrowed by someone')),
    #     ('archived', _('Archived - not available anymore')),
    # )

    country_name          = models.CharField(max_length=200)
    country_code          = models.CharField(max_length=3)
    # continent             = models.ForeignKey('continent.Continent', on_delete=models.PROTECT, related_name='countries')
    continent             = models.Choices('continent.Continent', on_delete=models.PROTECT, related_name='countries')

    def __str__(self):
        return self.country_name
