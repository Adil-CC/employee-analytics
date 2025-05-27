from django.db import models

# Create your models here.
class users(models.Model):
    name=models.CharField(max_length=52)
    passs=models.CharField(max_length=18)