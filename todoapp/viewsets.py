from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import TodoItem
from .serializer import TodoSerializer
from rest_framework import status


class TodoViewSet(ViewSet):
    """
        A simple viewset based controller to get todos
    """

    def list(self,request):
        todos = TodoItem.objects.all()
        if not todos:
            return Response({"message":"No todos found"})
        
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

