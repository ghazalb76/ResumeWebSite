#django imports
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    family_name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name
