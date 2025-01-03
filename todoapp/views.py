from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def start_app(request):
    return HttpResponse("Welcome to the Todo App")