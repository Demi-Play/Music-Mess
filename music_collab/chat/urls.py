from django.urls import path
from .views import ChatListView, ChatDetailView, ChatCreateView  # Импортируйте ChatCreateView

app_name = 'chat'

urlpatterns = [
    path('', ChatListView.as_view(), name='chat_list'),
    path('<int:pk>/', ChatDetailView.as_view(), name='chat_detail'),
    path('create/', ChatCreateView.as_view(), name='chat_create'),  # Добавьте этот маршрут
]