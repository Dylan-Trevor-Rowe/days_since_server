from dayssinceapi.models.Goals import Goals
from dayssinceapi.models.CheckedGoals import CheckedGoals
from dayssinceapi.models.DaysSinceUser import DaysSinceUser
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class CheckedGoalsViewset(ViewSet):

    def list(self, request):
        user = DaysSinceUser.objects.get(user=request.auth.user)
        goal = CheckedGoals.objects.all()
        goal.user = user
        # user_id = self.request.query_params.get('user_id', None)
        # if user_id is not None:
        #     goal = goal.filter(user_id=user_id)

        serializer = CheckedGoalsSerializer(
        goal, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):

        try:
            goals = CheckedGoals.objects.get(pk=pk)
            serializer = CheckedGoalsSerializer(goals, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
    
    def create(self, request):

        user = DaysSinceUser.objects.get(user=request.auth.user)

        goals = CheckedGoals()

        try:
            goals.date = request.data["date"]
            goals.checked = request.data["checked"]
            goal = Goals.objects.get(pk=request.data["goal"])
            goals.goal_id = goal.id
            goals.user = user
        except KeyError as ex:
            return Response({'message': 'Incorrect key was sent in request'}, status=status.HTTP_400_BAD_REQUEST)

     

        try:
            goals.save()
            serializer = CheckedGoalsSerializer(goals, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):

        try:
      
            goals = CheckedGoals.objects.get(pk=pk)
            goals.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Goals.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DaysSinceUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = DaysSinceUser
        fields = ['id', 'user']

class CheckedGoalsSerializer(serializers.ModelSerializer):
        user = DaysSinceUserSerializer(many=False)
        class Meta:
            model = CheckedGoals
            fields = ('id','date', 'checked', 'user', 'goal', )
            depth = 1
