from django.urls import path
from .views import ProjectDeleteView, ProjectEditView, ProjectListView, ProjectDetailView, ProjectCreateView, project_detail
from .views import AudioMaterialCreateView, AudioMaterialEditView, request_join_project, confirm_join_request
from django.conf import settings
from django.conf.urls.static import static


app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('create/', ProjectCreateView.as_view(), name='project_create'),
    path('<int:pk>/', project_detail, name='project_detail'),
    path('<int:pk>/edit/', ProjectEditView.as_view(), name='project_edit'),
    path('<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    
    path('<int:project_id>/audio/create/', AudioMaterialCreateView.as_view(), name='audio_material_create'),  # Добавьте этот маршрут
    path('<int:project_id>/audio/<int:audio_id>/edit/', AudioMaterialEditView.as_view(), name='audio_material_edit'),  # Добавьте этот маршрут
    
    path('<int:project_id>/request-join/', request_join_project, name='request_join'),  # Запрос на вхождение
    path('join-request/confirm/<int:request_id>/', confirm_join_request, name='confirm_join_request'),  
]
