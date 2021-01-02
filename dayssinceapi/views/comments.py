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
        depth = 2
        
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
        article = request.query_params.get('article', None)
        if article is not None:
            comments = comments.filter(article = article)
        serializer = CommentSerializer(
            comments, many=True, context={'request': request})
        return Response(serializer.data)

    def destroy(self, request, pk=None):

        try:
            comment = Comments.objects.get(pk=pk)
        except Comments.DoesNotExist as ex:
          
                return Response({'message': ex.args[0]})

        user = DaysSinceUser.objects.get(user=request.auth.user)
        if (comment.user != user):
            
           return Response(
                {'message': 'Articles can only be deleted by the users who authored them.'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        try:
            comment.delete()
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    