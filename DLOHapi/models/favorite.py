from django.db import models
from DLOHapi.models.destiny_inv import DestinyInventoryItems
from DLOHapi.models.dloh_user import DlohUser


class Favorite(models.Model):
    item = models.ForeignKey(DestinyInventoryItems, on_delete=models.CASCADE)
    dloh_user = models.ForeignKey(DlohUser, on_delete=models.CASCADE)
