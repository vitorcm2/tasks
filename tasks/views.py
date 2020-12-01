from django.shortcuts import render
from django.http import HttpResponse
from tasks.serializer import TaskSerializer
from tasks.models import Task


# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")


def get_tasks(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        tasks_list = TaskSerializer(tasks, many=True)
        return HttpResponse(tasks_list,content_type="application/json")