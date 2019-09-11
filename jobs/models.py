from django.db import models

# Create your models here.

class PastLife(models.Model):
    name = models.CharField(max_length=10)
    job = models.CharField(max_length=30)
    