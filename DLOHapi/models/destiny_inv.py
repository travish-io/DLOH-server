from django.db import models


class DestinyInventoryItems(models.Model):
    item_hash = models.BigIntegerField()
    description = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    icon = models.CharField(max_length=250)
    has_icon = models.BooleanField()
    tier_type = models.IntegerField()
    tier_type_name = models.CharField(max_length=25)
    item_type_name = models.CharField(max_length=50)
    item_type_tier_name = models.CharField(max_length=50)
    bucket_hash = models.BigIntegerField()
    is_instance_item = models.BooleanField()
