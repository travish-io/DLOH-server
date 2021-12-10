"""View module for handling requests about items"""
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from DLOHapi.models import DestinyInventoryItems


class DestinyInventoryItemsView(ViewSet):
    """Destiny Inventory Items"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single item

        Returns:
            Response -- JSON serialized game instance
        """
        try:
            # `pk` is a parameter to this function, and
            # Django parses it from the URL route parameter
            #   http://localhost:8000/games/2
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
        """Handle GET requests to games resource

        Returns:
            Response -- JSON serialized list of games
        """
        # Get all game records from the database
        items = DestinyInventoryItems.objects.all()

        # Support filtering games by type
        #    http://localhost:8000/games?type=1
        #
        # That URL will retrieve all tabletop games
        item_name = self.request.query_params.get('name', None)
        if item_name is not None:
            items = items.filter(name=item_name)

        serializer = InventoryItemSerializer(
            items, many=True, context={'request': request})
        return Response(serializer.data)


class InventoryItemSerializer(serializers.ModelSerializer):
    """JSON serializer for games

    Arguments:
        serializer type
    """
    class Meta:
        model = DestinyInventoryItems
        fields = ('id', 'item_hash', 'description', 'name',
                  'icon', 'has_icon', 'tier_type', 'tier_type_name', 'item_type_name', 'item_type_tier_name', 'bucket_hash', 'is_instance_item')
        depth = 1
