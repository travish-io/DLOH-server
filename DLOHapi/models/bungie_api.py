from django.db import models

class BungieApi(models.Model):
    membership_type = models.IntegerField()
    membership_id = models.CharField(max_length=50)
    character_id = models.CharField(max_length=50)
    item_instance_id = models.CharField(max_length=60)
    item_hash = models.IntegerField()
    bucket_hash = models.IntegerField()