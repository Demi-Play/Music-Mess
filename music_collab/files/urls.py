from django.urls import path
from .views import FileUploadView, FileListView

app_name = 'files'

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file_upload'),
    path('', FileListView.as_view(), name='file_list'),
]