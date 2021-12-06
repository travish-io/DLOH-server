from django.db import models
from django.contrib.auth.models import User
from DLOHapi.models.bungie_api import BungieApi


class DlohUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bungie_account = models.ForeignKey(
        BungieApi.membership_id, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
