from django.db import models
from DLOHapi.models.destiny_inv import DestinyInventoryItems
from DLOHapi.models.loadout import Loadout


class LoadoutInv(models.Model):
    item = models.ForeignKey(DestinyInventoryItems, on_delete=models.CASCADE)
    loadout = models.ForeignKey(Loadout, on_delete=models.CASCADE)
