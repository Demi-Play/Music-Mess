from django.urls import path
from .views import task_create, task_edit

app_name = 'tasks'

urlpatterns = [
    path('create/<int:project_id>/', task_create, name='task_create'),  # Создание задачи
    path('edit/<int:project_id>/<int:task_id>/', task_edit, name='task_edit'),  # Редактирование задачи
]