from django.urls import path
from .views import upload_file, file_list

app_name = 'version_control'

urlpatterns = [
    path('upload/<int:project_id>/', upload_file, name='upload_file'),
    path('files/<int:project_id>/', file_list, name='file_list'),
    # path('add-comment/<int:file_id>/', add_comment, name='add_comment'),
]