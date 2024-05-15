from django.db import models


class Driver(models.Model):
    reference = models.CharField(max_length=128)
    number = models.CharField(max_length=3)
    code = models.CharField(max_length=3)
    given_name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    dob = models.DateField()
    nationality = models.CharField(max_length=64)
    wiki_url = models.URLField()
