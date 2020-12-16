from dayssinceapi.models import Comments, Articles
from dayssinceapi.models.DaysSinceUser import DaysSinceUser
from django.core.exceptions import ValidationError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

class DaysSinceUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = DaysSinceUser
        fields = ['id', 'user']

class CommentSerializer(serializers.ModelSerializer):

    user = DaysSinceUser()
    
    class Meta:
        model = Comments
        fields = ('id','user', 'comment', 'article' ,)
        
class CommentViewSet(ViewSet):

    def create(self, request):

        user = DaysSinceUser.objects.get(user=request.auth.user)
        comment = Comments()
     
        try:
            comment.comment = request.data["comment"]
            articles = Articles.objects.get(pk=request.data["article"])
            comment.article_id = articles.id

        except KeyError as ex:
            return Response({'message': 'Incorrect key was sent in request'}, status=status.HTTP_400_BAD_REQUEST)

        comment.user = user
      
        try:
            comment.save()
            serializer = CommentSerializer(comment, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
     
        comments = Comments.objects.all()
        ArticleId = request.query_params.get('articleId', None)
        if ArticleId is not None:
            comments = comments.filter(articleId = ArticleId)
        serializer = CommentSerializer(
            comments, many=True, context={'request': request})
        return Response(serializer.data)

    def destroy(self, request, pk=None):

        try:
            comments = Comments.objects.get(pk=pk)
            comments.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Comments.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    