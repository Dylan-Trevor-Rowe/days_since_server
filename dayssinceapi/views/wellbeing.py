from django.contrib.auth.models import User
from dayssinceapi.models.DaysSinceUser import DaysSinceUser
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from django.db.models import Count, Q
from dayssinceapi.models import WellBeing, DaysSinceUser
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

class WellBeing(ViewSet):
    """Emotional Well Being"""

    def list(self, request):
        """Handle GET requests to games resource
        Returns:
            Response -- JSON serialized list of games
        """
        user = DaysSinceUser.objects.get(user=request.auth.user)

   
        serializer = WellBeingSerializer(
         many=True, context={'request': request})
        return Response(serializer.data)

class WellBeingSerializer(serializers.ModelSerializer):
    """JSON serializer for games"""

gamer = WellBeingSerializer(many=False)

class Meta:
        model = WellBeing
        fields = ('id',' date', 'fatigueScale', 'painScale','symptoms', 'hoursOfSleep', 'emotionalWellBeing')
        depth = 1