#django imports
from django.db import models


class Users(models.Model):

    username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=32)
    repass = models.CharField(max_length=32)

    def __str__(self):
        return self.name
