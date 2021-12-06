from django.db import models
from DLOHapi.models.bungie_api import BungieApi
from DLOHapi.models.dloh_user import DlohUser


class Favorite(models.Model):
    item = models.ForeignKey(BungieApi, on_delete=models.CASCADE)
    dloh_user = models.ForeignKey(DlohUser, on_delete=models.CASCADE)
