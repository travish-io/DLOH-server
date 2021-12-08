from django.db import models


class DestinyInventoryItems(models.Model):
    item_hash = models.IntegerField()
    description = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    icon = models.CharField(max_length=250)
    has_icon = models.BooleanField()
    flavor_text = models.CharField(max_length=250)
    tier_type = models.IntegerField()
    tier_name = models.CharField(max_length=25)
    bucket_hash = models.IntegerField()
    is_instance_item = models.BooleanField()
