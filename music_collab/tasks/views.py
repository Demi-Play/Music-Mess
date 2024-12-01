from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm  # Импортируем форму для задач
from projects.models import Project  # Импортируем модель Project
from django.contrib.auth.decorators import login_required

@login_required
def task_create(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project  # Привязываем задачу к проекту
            task.save()
            return redirect('projects:project_detail', pk=project.id)
    else:
        form = TaskForm()
    
    return render(request, 'tasks/task_form.html', {'form': form, 'project': project})

@login_required
def task_edit(request, project_id, task_id):
    task = get_object_or_404(Task, pk=task_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('projects:project_detail', pk=project_id)
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/task_form.html', {'form': form, 'project': task.project})