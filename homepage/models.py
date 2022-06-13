from django.db import models

# Create your models here.
class Person(models.Model):
    email = models.CharField(max_length=50)
    organization = models.CharField(max_length=50, default="N/A")
    message = models.CharField(max_length=500)
    reason = models.CharField(max_length=20)
