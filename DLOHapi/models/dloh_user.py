from django.db import models
from django.contrib.auth.models import User


class DlohUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bungie_id = models.IntegerField()
