from http import HTTPStatus
from telnetlib import STATUS
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TaskSerializer
from .models import Task

# Create your views here.

@api_view(['GET'])
def apiTest(request):
    return Response("API TEST")

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    taskList = TaskSerializer(tasks, many=True)
    return Response(taskList.data)

@api_view(['POST'])
def taskCreate(request):
    task = TaskSerializer(data=request.data)

    if task.is_valid():
        task.save()
    
    return Response(task.data, status=HTTPStatus.CREATED)

@api_view(['GET'])
def taskById(request, pk):
    tasks = Task.objects.get(id=pk)
    taskList = TaskSerializer(tasks, many=False)

    return Response(taskList.data)

@api_view(['DELETE'])
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response("Task Deleted Successfully !")