"""View module for handling requests about games"""
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from DLOHapi.models import DlohUser, Loadout, LoadoutInv, dloh_user
from django.db.models import Q
from rest_framework.decorators import action

from DLOHapi.models.destiny_inv import DestinyInventoryItems


class LoadoutView(ViewSet):
    """Destiny Loadout Helper"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized game instance
        """

        # Uses the token passed in the `Authorization` header
        dloh_user = DlohUser.objects.get(user=request.auth.user)

        # Try to save the new game to the database, then
        # serialize the game instance as JSON, and send the
        # JSON as a response to the client request
        try:
            # Create a new Python instance of the Game class
            # and set its properties from what was sent in the
            # body of the request from the client.
            loadout = Loadout.objects.create(
                name=request.data["name"],
                dloh_user=dloh_user,
            )
            loadout.destiny_items_list.set(request.data['loadoutItemsList'])
            serializer = LoadoutSerializer(
                loadout, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # If anything went wrong, catch the exception and
        # send a response with a 400 status code to tell the
        # client that something was wrong with its request data
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    # TO DO: refactor this signup method to add items to destiny_items_list for create method

    @action(methods=['post'], detail=True)
    def additem(self, request, pk=None):
        """Adds items from armory list to new loadout"""
        # Django uses the `Authorization` header to determine
        # which user is making the request to sign up
        dloh_user = DlohUser.objects.get(user=request.auth.user)

        loadout = Loadout.objects.create()

        try:
            # Handle the case if the client specifies a game
            # that doesn't exist
            item = DestinyInventoryItems.objects.get(pk=pk)
        except DestinyInventoryItems.DoesNotExist:
            return Response(
                {'message': 'Event does not exist.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # A gamer wants to sign up for an event
        if request.method == "POST":
            try:
                # Using the attendees field on the event makes it simple to add a gamer to the event
                # .add(gamer) will insert into the join table a new row the gamer_id and the event_id
                item.destiny_items_list.add()
                return Response({}, status=status.HTTP_201_CREATED)
            except Exception as ex:
                return Response({'message': ex.args[0]})

        # User wants to leave a previously joined event
        elif request.method == "DELETE":
            try:
                # The many to many relationship has a .remove method that removes the gamer from the attendees list
                # The method deletes the row in the join table that has the gamer_id and event_id
                event.attendees.remove(gamer)
                return Response(None, status=status.HTTP_204_NO_CONTENT)
            except Exception as ex:
                return Response({'message': ex.args[0]})

    def retrieve(self, request, pk=None):
        """Handle GET requests for single loadout

        Returns:
            Response -- JSON serialized loadout instance
        """
        try:
            # `pk` is a parameter to this function, and
            # Django parses it from the URL route parameter
            #   http://localhost:8000/loadouts/2
            #
            # The `2` at the end of the route becomes `pk`
            loadout = Loadout.objects.get(pk=pk)
            serializer = LoadoutSerializer(
                loadout, context={'request': request})
            return Response(serializer.data)
        except Loadout.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return HttpResponseServerError(ex)

    # def update(self, request, pk=None):
    #     """Handle PUT requests for a game

    #     Returns:
    #         Response -- Empty body with 204 status code
    #     """
    #     gamer = Gamer.objects.get(user=request.auth.user)

    #     # Do mostly the same thing as POST, but instead of
    #     # creating a new instance of Game, get the game record
    #     # from the database whose primary key is `pk`
    #     game = Game.objects.get(pk=pk)
    #     game.title = request.data["title"]
    #     game.maker = request.data["maker"]
    #     game.number_of_players = request.data["numberOfPlayers"]
    #     game.skill_level = request.data["skillLevel"]
    #     game.gamer = gamer

    #     game_type = GameType.objects.get(pk=request.data["gameTypeId"])
    #     game.game_type = game_type
    #     game.save()

    #     # 204 status code means everything worked but the
    #     # server is not sending back any data in the response
    #     return Response({}, status=status.HTTP_204_NO_CONTENT)

    # def destroy(self, request, pk=None):
    #     """Handle DELETE requests for a single game

    #     Returns:
    #         Response -- 200, 404, or 500 status code
    #     """
    #     try:
    #         game = Game.objects.get(pk=pk)
    #         game.delete()

    #         return Response({}, status=status.HTTP_204_NO_CONTENT)

    #     except Game.DoesNotExist as ex:
    #         return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    #     except Exception as ex:
    #         return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to loadouts resource

        Returns:
            Response -- JSON serialized list of loadouts
        """
        # get current dloh_user
        dloh_user = DlohUser.objects.get(user=request.auth.user)
        # filter loadouts by current dloh_user
        loadouts = Loadout.objects.filter(dloh_user_id=dloh_user.id)

        serializer = LoadoutSerializer(
            loadouts, many=True, context={'request': request})
        return Response(serializer.data)


class LoadoutSerializer(serializers.ModelSerializer):
    """JSON serializer for loadouts

    Arguments:
        serializer type
    """
    class Meta:
        model = Loadout
        fields = ('id', 'name', 'dloh_user', 'destiny_items_list')
        depth = 2
