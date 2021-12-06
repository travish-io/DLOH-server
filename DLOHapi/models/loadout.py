from django.db import models
from DLOHapi.models.dloh_user import DlohUser


class Loadout(models.Model):
    name = models.CharField(max_length=50)
    dloh_user = models.ForeignKey(DlohUser, on_delete=models.CASCADE)
    