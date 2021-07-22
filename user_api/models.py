from django.db import models


class CustomUser(models.Model):
    username = models.CharField(max_length=40, unique=True)
    first_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=40, blank=True, null=True)
    password = models.CharField(max_length=40)
    email = models.CharField(max_length=40, blank=True, null=True)


