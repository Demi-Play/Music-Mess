from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Project, JoinRequest
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Project, AudioMaterial
from .forms import AudioMaterialForm

@method_decorator(login_required, name='dispatch')
class ProjectListView(View):
    def get(self, request):
        projects = Project.objects.all()
        return render(request, 'projects/project_list.html', {'projects': projects})



@method_decorator(login_required, name='dispatch')
class ProjectDetailView(View):
    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        audio_materials = project.audio_materials.all()
        return render(request, 'projects/project_detail.html', {'project': project, 'audio_materials': audio_materials})

@method_decorator(login_required, name='dispatch')
class AudioMaterialCreateView(View):
    def get(self, request, project_id):
        form = AudioMaterialForm()
        return render(request, 'projects/audio_material_form.html', {'form': form, 'project_id': project_id})

    def post(self, request, project_id):
        form = AudioMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            audio_material = form.save(commit=False)
            audio_material.project = get_object_or_404(Project, pk=project_id)
            audio_material.save()
            return redirect('projects:project_detail', pk=project_id)
        return render(request, 'projects/audio_material_form.html', {'form': form, 'project_id': project_id})

@method_decorator(login_required, name='dispatch')
class AudioMaterialEditView(View):
    def get(self, request, project_id, audio_id):
        audio_material = get_object_or_404(AudioMaterial, pk=audio_id)
        form = AudioMaterialForm(instance=audio_material)
        return render(request, 'projects/audio_material_form.html', {'form': form, 'project_id': project_id})

    def post(self, request, project_id, audio_id):
        audio_material = get_object_or_404(AudioMaterial, pk=audio_id)
        form = AudioMaterialForm(request.POST, request.FILES, instance=audio_material)
        if form.is_valid():
            form.save()
            return redirect('projects:project_detail', pk=project_id)
        return render(request, 'projects/audio_material_form.html', {'form': form, 'project_id': project_id})

@method_decorator(login_required, name='dispatch') 
class ProjectCreateView(View):
    def get(self, request):
        form = ProjectForm()
        return render(request, 'projects/project_form.html', {'form': form})

    def post(self, request):
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user  # Устанавливаем владельца проекта
            project.save()
            return redirect('projects:project_list')
        return render(request, 'projects/project_form.html', {'form': form})
    
@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)

    # Проверяем доступ пользователя
    if request.user != project.owner and not project.join_requests.filter(user=request.user, confirmed=True).exists():
        return render(request, '403.html', {'project': project})  # Отображаем страницу 403

    return render(request, 'projects/project_detail.html', {'project': project})

@login_required
def request_join_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    
    if request.method == 'POST':
        join_request = JoinRequest.objects.create(project=project, user=request.user)
        return redirect('projects:project_detail', pk=project.id)

    return render(request, 'projects/request_join.html', {'project': project})

@login_required
def confirm_join_request(request, request_id):
    join_request = get_object_or_404(JoinRequest, pk=request_id)

    if request.user == join_request.project.owner:
        join_request.confirmed = True
        join_request.save()
        # Здесь можно добавить логику для добавления пользователя в проект
        return redirect('projects:project_detail', pk=join_request.project.id)
    
    return redirect('projects:project_list')  # Перенаправляем на список проектов