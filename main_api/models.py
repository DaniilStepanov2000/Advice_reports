from django.db import models
from django.contrib.auth.models import User


class Report(models.Model):
    title = models.CharField(max_length=20, null=True)
    time = models.TimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
