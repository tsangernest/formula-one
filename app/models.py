from django.db import models


class Driver(models.Model):
    reference = models.CharField(max_length=128)
    number = models.IntegerField(max_length=100)
    code = models.CharField(max_length=3)
    given_name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    dob = models.DateTimeField()
    nationality = models.CharField(max_length=64)
    wiki_url = models.URLField()
