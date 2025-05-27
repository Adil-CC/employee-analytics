# accounts/models.py
from django.db import models

class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # store hashed passwords in real apps!

    def __str__(self):
        return self.username
