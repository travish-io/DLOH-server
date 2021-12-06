from django.db import models
from DLOHapi.models.bungie_api import BungieApi
from DLOHapi.models.loadout import Loadout


class LoadoutInv(models.Model):
    item = models.ForeignKey(BungieApi, on_delete=models.CASCADE)
    loadout = models.ForeignKey(Loadout, on_delete=models.CASCADE)
