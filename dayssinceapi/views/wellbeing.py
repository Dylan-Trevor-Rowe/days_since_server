from dayssinceapi.models.DaysSinceUser import DaysSinceUser
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from django.db.models import Count, Q
from dayssinceapi.models import WellBeing
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class WellBeingView(ViewSet):
    """Emotional Well Being"""

    def list(self, request):
   
        wellbeing = WellBeing.objects.all()
        serializer = WellBeingSerializer(
        wellbeing, many=True)
        return Response(serializer.data)

    def create(self, request):

        user = DaysSinceUser.objects.get(user=request.auth.user)

        well_being = WellBeing()
        well_being.user = user

        try:
            well_being.date = request.data["date"]
            well_being.fatigueScale = request.data["fatigueScale"]
            well_being.painScale = request.data["painScale"]
            well_being.noSymptoms = request.data["noSymptoms"]
            well_being.numbness = request.data["numbness"]
            well_being.tingling = request.data["tingling"]
            well_being.weakness = request.data["weakness"]
            well_being.stiffness = request.data["stiffness"]
            well_being.coordinationOrBalanceProblems = request.data["coordinationOrBalanceProblems"]
            well_being.heatSensitivity = request.data["heatSensitivity"]
            well_being.incontenance = request.data["incontenance"]
            well_being.brainFog = request.data["brainFog"]
            well_being.hoursOfSleep = request.data["hoursOfSleep"]
            well_being.emotionalWellBeing = request.data["emotionalWellBeing"]
        
        except KeyError as ex:
            return Response({'message': 'Incorrect key was sent in request'}, status=status.HTTP_400_BAD_REQUEST)

        well_being.user = user

        try:
            well_being.save()
            serializer = WellBeingSerializer(well_being, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):

        try:
            well_being = WellBeing.objects.get(pk=pk)
            well_being.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except WellBeing.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve(self, request, pk=None):
     
        try:
            well_being = WellBeing.objects.get(pk=pk)
            serializer = WellBeingSerializer(well_being, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
   
        user = DaysSinceUser.objects.get(user=request.auth.user)

        well_being = WellBeing.objects.get(pk=pk)
        well_being.date = request.data["date"]
        well_being.fatigueScale = request.data["fatigueScale"]
        well_being.painScale = request.data["painScale"]
        well_being.noSymptoms = request.data["noSymptoms"]
        well_being.numbness = request.data["numbness"]
        well_being.tingling = request.data["tingling"]
        well_being.weakness = request.data["weakness"]
        well_being.stiffness = request.data["stiffness"]
        well_being.coordinationOrBalanceProblems = request.data["coordinationOrBalanceProblems"]
        well_being.heatSensitivity = request.data["heatSensitivity"]
        well_being.incontenance = request.data["incontenance"]
        well_being.brainFog = request.data["brainFog"]
        well_being.hoursOfSleep = request.data["hoursOfSleep"]
        well_being.emotionalWellBeing = request.data["emotionalWellBeing"]
        well_being.user = user
        well_being.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

      
class WellBeingSerializer(serializers.ModelSerializer):
    """JSON serializer for WellBeing"""

    class Meta:
        model = WellBeing
        fields = ('id','date','weakness', 'stiffness', 'coordinationOrBalanceProblems', 'heatSensitivity', 'incontenance', 'brainFog', 'fatigueScale', 'painScale','noSymptoms', 'numbness', 
        'tingling',  'hoursOfSleep', 'emotionalWellBeing' ,)
        depth = 1


        