from django.shortcuts import render, redirect
from django.views import View
from .models import File
from .forms import FileUploadForm

class FileUploadView(View):
    def get(self, request):
        form = FileUploadForm()
        return render(request, 'files/file_upload.html', {'form': form})

    def post(self, request):
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.uploaded_by = request.user  # Устанавливаем пользователя загрузившего файл
            file_instance.save()
            return redirect('files:file_list')
        return render(request, 'files/file_upload.html', {'form': form})

class FileListView(View):
    def get(self, request):
        files = File.objects.all()
        return render(request, 'files/file_list.html', {'files': files})