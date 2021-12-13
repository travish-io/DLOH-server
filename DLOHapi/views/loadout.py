"""View module for handling requests about games"""
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from DLOHapi.models import DlohUser, Loadout, LoadoutInv
from django.db.models import Q


class LoadoutView(ViewSet):
    """Destiny Loadout Helper"""

    # def create(self, request):
    #     """Handle POST operations

    #     Returns:
    #         Response -- JSON serialized game instance
    #     """

    #     # Uses the token passed in the `Authorization` header
    #     loadout = Loadout.objects.get(user=request.auth.user)

    #     # Use the Django ORM to get the record from the database
    #     # whose `id` is what the client passed as the
    #     # `gameTypeId` in the body of the request.
    #     loadout_inv = LoadoutInv.objects.get(pk=request.data["loadoutInvId"])

    #     # Try to save the new game to the database, then
    #     # serialize the game instance as JSON, and send the
    #     # JSON as a response to the client request
    #     try:
    #         # Create a new Python instance of the Game class
    #         # and set its properties from what was sent in the
    #         # body of the request from the client.
    #         game = Game.objects.create(
    #             title=request.data["title"],
    #             maker=request.data["maker"],
    #             number_of_players=request.data["numberOfPlayers"],
    #             skill_level=request.data["skillLevel"],
    #             gamer=gamer,
    #             game_type=game_type
    #         )
    #         serializer = GameSerializer(game, context={'request': request})
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    #     # If anything went wrong, catch the exception and
    #     # send a response with a 400 status code to tell the
    #     # client that something was wrong with its request data
    #     except ValidationError as ex:
    #         return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

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
