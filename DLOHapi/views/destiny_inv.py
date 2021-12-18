"""View module for handling requests about items"""
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from DLOHapi.models import DestinyInventoryItems
from django.db.models import Q


class DestinyInventoryItemsView(ViewSet):
    """Destiny Inventory Items(Armory)"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single item

        Returns:
            Response -- JSON serialized item instance
        """
        try:
            # `pk` is a parameter to this function, and
            # Django parses it from the URL route parameter
            #   http://localhost:8000/Armory/2
            #
            # The `2` at the end of the route becomes `pk`
            item = DestinyInventoryItems.objects.get(pk=pk)
            serializer = InventoryItemSerializer(
                item, context={'request': request})
            return Response(serializer.data)
        except DestinyInventoryItems.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to armory resource

        Returns:
            Response -- JSON serialized list of armory items
        """
        # filtering unwanted items from the db
        items = DestinyInventoryItems.objects.filter(
            ~Q(item_type_tier_name__contains='Legendary Chest Armor'), ~Q(item_type_tier_name__contains='Legendary Gauntlets'), ~Q(item_type_tier_name__contains='Legendary Helmet'), ~Q(item_type_tier_name__contains='Legendary Leg Armor'))

        # trying to find a way to filter duplicates from different seasons
        items = items.distinct()

        # Setting up query params
        # http://localhost:8000/Armory?param=Exotic Hand Cannon
        #
        # That URL will retrieve all Exotic Hand Cannons
        item_param = self.request.query_params.get('param', None)
        if item_param is not None:
            items = items.filter(Q(name__contains=item_param) | Q(
                item_type_tier_name__contains=item_param))

        serializer = InventoryItemSerializer(
            items, many=True, context={'request': request})
        return Response(serializer.data)


class InventoryItemSerializer(serializers.ModelSerializer):
    """JSON serializer for armory items

    Arguments:
        serializer type
    """
    class Meta:
        model = DestinyInventoryItems
        fields = ('id', 'item_hash', 'description', 'name',
                  'icon', 'has_icon', 'tier_type', 'tier_type_name', 'item_type_name', 'item_type_tier_name', 'bucket_hash', 'is_instance_item')
        depth = 1
