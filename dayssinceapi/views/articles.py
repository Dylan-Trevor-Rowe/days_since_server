from dayssinceapi.models import Articles
from dayssinceapi.models.DaysSinceUser import DaysSinceUser
from django.core.exceptions import ValidationError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

class ArticlesViewset(ViewSet):

    def list(self, request):
   
        articles = Articles.objects.all()
   
        serializer = ArticleSerializer(
        articles, many=True)
        return Response(serializer.data)

    def create(self, request):

        user = DaysSinceUser.objects.get(user=request.auth.user)

        articles = Articles()

        try:
            articles.date = request.data["date"]
            articles.title = request.data["title"]
            articles.link = request.data['link']
            articles.user = user
      
        except KeyError as ex:
            return Response({'message': 'Incorrect key was sent in request'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            articles.save()
            serializer = ArticleSerializer(articles, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):

        try:
            articles = Articles.objects.get(pk=pk)
            articles.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Articles.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ArticleSerializer(serializers.ModelSerializer):
    # link = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    
    # )

  
    class Meta:
        model = Articles
        fields = ('id','date', 'title', 'link', 'user' )
        depth = 1

