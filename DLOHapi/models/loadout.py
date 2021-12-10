from django.db import models
from DLOHapi.models.destiny_inv import DestinyInventoryItems
from DLOHapi.models.dloh_user import DlohUser


class Loadout(models.Model):
    name = models.CharField(max_length=50)
    dloh_user = models.ForeignKey(DlohUser, on_delete=models.CASCADE)
    destiny_items_list = models.ManyToManyField(
        DestinyInventoryItems, through="LoadoutInv", related_name="loadouts_list")
