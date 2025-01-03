from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import TodoItem
from .serializer import TodoSerializer


# Create your views here.
def start_app(request):
    return HttpResponse("Welcome to the Todo App")

@api_view(["GET"])
def all_todos(request):
    todos = TodoItem.objects.all()
    if len(todos) == 0:
        return Response({"message":"No todos found"})
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data , status=status.HTTP_200_OK)

@api_view(["POST"])
def post_todo(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
