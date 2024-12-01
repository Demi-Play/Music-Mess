from django.urls import path
from .views import ProjectListView, ProjectDetailView, ProjectCreateView, project_detail
from .views import AudioMaterialCreateView, AudioMaterialEditView, request_join_project, confirm_join_request

app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('create/', ProjectCreateView.as_view(), name='project_create'),
    path('<int:pk>/', project_detail, name='project_detail'),
    
    path('<int:project_id>/audio/create/', AudioMaterialCreateView.as_view(), name='audio_material_create'),  # Добавьте этот маршрут
    path('<int:project_id>/audio/<int:audio_id>/edit/', AudioMaterialEditView.as_view(), name='audio_material_edit'),  # Добавьте этот маршрут
    
    path('<int:project_id>/request-join/', request_join_project, name='request_join'),  # Запрос на вхождение
    path('join-request/<int:request_id>/confirm/', confirm_join_request, name='confirm_join_request'),  
]