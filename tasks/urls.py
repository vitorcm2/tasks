from django.urls import path
from . import views

urlpatterns = [
    path('get_all_tasks', views.get_all_tasks, name='get_all_tasks'),
    path('get_task/<int:task_id>', views.get_task, name='get_task'),
    path('edit_task/<int:task_id>', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>', views.delete_task, name='delete_task'),
    path('create_task', views.create_task, name='create_task'),
]
