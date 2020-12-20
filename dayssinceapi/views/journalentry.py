from dayssinceapi.models.JournalEntry import JournalEntry
from dayssinceapi.models.DaysSinceUser import DaysSinceUser
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class JournalEntryView(ViewSet):

    def list(self, request):
   
        journal_entry = JournalEntry.objects.all()
   
        serializer = JournalEntrySerializer(
        journal_entry, many=True)
        return Response(serializer.data)

    def create(self, request):

        user = DaysSinceUser.objects.get(user=request.auth.user)

        journal_entry =JournalEntry()

        try:
            journal_entry.date = request.data["date"]
            journal_entry.entry = request.data["entry"]
        except KeyError as ex:
            return Response({'message': 'Incorrect key was sent in request'}, status=status.HTTP_400_BAD_REQUEST)

        journal_entry.user = user

        try:
            journal_entry.save()
            serializer = JournalEntrySerializer(journal_entry, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):

        try:
            journal_entry = JournalEntry.objects.get(pk=pk)
            journal_entry.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except JournalEntry.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def retrieve(self, request, pk=None):
     
        try:
            journal_entry = JournalEntry.objects.get(pk=pk)
            serializer = JournalEntrySerializer(journal_entry, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
   
        user = DaysSinceUser.objects.get(user=request.auth.user)
        jounral_entry = JournalEntry.objects.get(pk=pk)
        jounral_entry.date = request.data["date"]
        jounral_entry.entry = request.data["entry"]
        jounral_entry.user = user
        jounral_entry.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

      
class JournalEntrySerializer(serializers.ModelSerializer):
    """JSON serializer for Journal"""

    class Meta:
        model = JournalEntry
        fields = ('id','date', 'entry', )
        depth = 1

class DaysSinceUserSerializer(serializers.ModelSerializer):

        class Meta:
            model = DaysSinceUser
            fields = ['id', 'user']


        