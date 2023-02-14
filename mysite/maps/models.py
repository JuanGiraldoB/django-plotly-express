from django.db import models

# Create your models here.


class AudioLabel(models.Model):
    frequency1 = models.FloatField()
    frequency2 = models.FloatField()
    time1 = models.FloatField()
    time2 = models.FloatField()


class FileName(models.Model):
    fileNames = models.TextField()
