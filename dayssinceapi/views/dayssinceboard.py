from dayssinceapi.models import DaysSinceBoard
from dayssinceapi.models.DaysSinceUser import DaysSinceUser, username
from django.core.exceptions import ValidationError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

class DaysSinceBoardView(ViewSet):

    def list(self, request):
   
        board = DaysSinceBoard.objects.all()
        user = DaysSinceUser.objects.get(user=request.auth.user)
   
        serializer = DaysSinceBoardSerializer(
        board, many=True)
        return Response(serializer.data)

    def create(self, request):

        user = DaysSinceUser.objects.get(user=request.auth.user)

        board = DaysSinceBoard()

        try:
            board.daysSinceBoard = request.data["daysSinceBoard"]
            board.daysSinceBoard = request.data['created']
            board.user = user
      
        except KeyError as ex:
            return Response({'message': 'Incorrect key was sent in request'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            board.save()
            serializer = DaysSinceBoardSerializer(board, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)


class DaysSinceBoardSerializer(serializers.ModelSerializer):
  
        class Meta:
            model = DaysSinceBoard
            fields = ('id', 'daysSinceBoard', 'created', 'user', )
            depth = 1
