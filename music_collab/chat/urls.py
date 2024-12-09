from django.urls import path
from .views import ChatListView, ChatDetailView, ChatCreateView

app_name = 'chat'

urlpatterns = [
    path('', ChatListView.as_view(), name='chat_list'),
    path('<int:pk>/', ChatDetailView.as_view(), name='chat_detail'),
    path('create/', ChatCreateView.as_view(), name='chat_create'),
    path('messages/<int:message_id>/edit/', ChatDetailView.as_view(), name='edit_message'),  # Новый маршрут для редактирования
    path('messages/<int:message_id>/delete/', ChatDetailView.as_view(), name='delete_message'),  # Новый маршрут для удаления
  # Новый маршрут
]