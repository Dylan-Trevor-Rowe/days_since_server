from dayssinceapi.models.Goals import Goals
from dayssinceapi.models.DaysSinceUser import DaysSinceUser
from django.core.exceptions import ValidationError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class GoalsViewset(ViewSet):

    def list(self, request):
   
        goal = Goals.objects.all()
   
        serializer = GoalSerializer(
        goal, many=True)
        return Response(serializer.data)

    def create(self, request):

        user = DaysSinceUser.objects.get(user=request.auth.user)

        goals = Goals()

        try:
            goals.date = request.data["date"]
            goals.goal_name = request.data["goal_name"]
        except KeyError as ex:
            return Response({'message': 'Incorrect key was sent in request'}, status=status.HTTP_400_BAD_REQUEST)

        goals.user = user

        try:
            goals.save()
            serializer = GoalSerializer(goals, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):

        try:
            goals = Goals.objects.get(pk=pk)
            goals.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Goals.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk=None):
   
        user = DaysSinceUser.objects.get(user=request.auth.user)
        goals = Goals.objects.get(pk=pk)
        goals.date = request.data["date"]
        goals.goal_name = request.data["goal_name"]
        goals.user = user
        goals.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

      
class GoalSerializer(serializers.ModelSerializer):
    """JSON serializer for Journal"""

    class Meta:
        model = Goals
        fields = ('id','date', 'goal_name', )
        depth = 1

