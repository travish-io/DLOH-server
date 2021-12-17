"""
seed the db:
python3 manage.py seed_db
(file name)
    """

from django.core.management.base import BaseCommand
import requests
from DLOHapi.models import DestinyInventoryItems


class Command(BaseCommand):
    def handle(self, *args, **options):
        DestinyInventoryItems.objects.all().delete()
        response = requests.get(
            "https://www.bungie.net/common/destiny2_content/json/en/DestinyInventoryItemLiteDefinition-a0921ed4-d9c4-4881-ad7a-999cb843d6a3.json")
        json = response.json()
        for item in json:
            display_properties = json[item]['displayProperties']
            inventory = json[item]['inventory']
            if inventory.get('tierTypeName', "") in ["", 'Legendary', 'Exotic'] and display_properties['hasIcon'] and inventory.get('bucketTypeHash') in [1498876634, 2465295065, 953998645, 3448274439, 3551918588, 14239492, 20886954, 158578786] and inventory['isInstanceItem']:
                new_destiny_item = DestinyInventoryItems.objects.create(
                    item_hash=item,
                    description=display_properties['description'],
                    name=display_properties['name'],
                    icon=display_properties.get('icon', ""),
                    has_icon=display_properties['hasIcon'],
                    tier_type=inventory['tierType'],
                    tier_type_name=inventory.get('tierTypeName', ""),
                    item_type_name=json[item]['itemTypeDisplayName'],
                    item_type_tier_name=json[item]['itemTypeAndTierDisplayName'],
                    bucket_hash=inventory['bucketTypeHash'],
                    is_instance_item=inventory['isInstanceItem']
                )

# working api url:  https://www.bungie.net/common/destiny2_content/json/en/DestinyInventoryItemLiteDefinition-a0921ed4-d9c4-4881-ad7a-999cb843d6a3.json
