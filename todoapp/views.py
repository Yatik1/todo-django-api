from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import TodoItem
from .serializer import TodoSerializer


# Create your views here.
def start_app(request):
    return HttpResponse({"message":"This is api start route for todo app"})

# get request to fetch all todos from the database
@api_view(["GET"])
def all_todos(request):
    todos = TodoItem.objects.all()
    if len(todos) == 0:
        return Response({"message":"No todos found"})
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data , status=status.HTTP_200_OK)

# post request to add new todo in the database
@api_view(["POST"])
def post_todo(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# put request to update the todo details in the database
@api_view(["PUT"])
def update_todo(request,pk):
    try:
        todo = TodoItem.objects.get(pk=pk)
    except:
        return Response({"message":"Todo not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = TodoSerializer(todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete_todo(request,pk):
    try:
        todo = TodoItem.objects.get(pk=pk)
    except:
        return Response({'message':'Todo not found'},status=status.HTTP_404_NOT_FOUND)
    
    todo.delete()
    return Response({'message':"Todo deleted successfullt"},status=status.HTTP_200_OK)
