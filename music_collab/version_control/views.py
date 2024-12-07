from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import FileUploadForm
from projects.models import Project
from .models import File, AudioComment

@login_required
def upload_file(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.project = project
            file_instance.uploaded_by = request.user
            file_instance.save()
            return redirect('version_control:file_list', project_id=project.id)
    else:
        form = FileUploadForm()

    return render(request, 'version_control/upload_file.html', {'form': form, 'project': project})

@login_required
def file_list(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    files = project.audio_materials.all()  # Или используйте File.objects.filter(project=project)

    return render(request, 'version_control/file_list.html', {'files': files, 'project': project})

@login_required
def add_comment(request, file_id):
    file_instance = get_object_or_404(File, pk=file_id)

    if request.method == 'POST':
        text = request.POST.get('text')
        timestamp = request.POST.get('timestamp')
        comment = AudioComment.objects.create(file=file_instance, user=request.user, text=text, timestamp=timestamp)
        return redirect('version_control:file_list', project_id=file_instance.project.id)

    return render(request, 'version_control/add_comment.html', {'file': file_instance})