from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from tasks.models import Task
from django.core import serializers
from tasks.serializer import TaskSerializer
from rest_framework.parsers import JSONParser
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view



# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the tasks index.")

@api_view(["GET"])
def get_all_tasks(request):
        tasks = Task.objects.all()
        tasks_list = serializers.serialize("json",tasks)
        return HttpResponse(tasks_list,content_type="application/json")

@api_view(["GET"]) 
def get_task(request,task_id):
        try:
            task = Task.objects.get(pk=task_id)
            return JsonResponse(model_to_dict(task),safe=False)
        except:
            return Http404("Id não encontrado")
        
@api_view(["PUT"])
def edit_task(request,task_id):
        try:
            task = Task.objects.get(pk=task_id)
            request_data = JSONParser().parse(request)
            task.title = request_data["title"]
            task.description = request_data["description"]
            task.pub_date = request_data["pub_date"]
            task.save()
            return JsonResponse(model_to_dict(task),safe=False,status=201)
        except:
            return Http404("Id não encontrado")
            
            
@api_view(["DELETE"])
def delete_task(request, task_id):
        try:
            task = Task.objects.get(pk=task_id)
            task.delete()
            return HttpResponse("Task apagado com sucesso")
        
        except:
            return Http404("Id não encontrado")
        
@api_view(["POST"])
def create_task(request):
        request_data = JSONParser().parse(request)
        task = TaskSerializer(data=request_data)
        if task.is_valid():
            task.save()
            return JsonResponse(task.data,safe=False,status=201)
        else:
            return JsonResponse(task.errors,safe=False,status=400)
        

