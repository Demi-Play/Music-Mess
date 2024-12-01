from django.urls import path
from .views import AudioCommentListView, AudioCommentCreateView

app_name = 'comments'

urlpatterns = [
    path('', AudioCommentListView.as_view(), name='audio_comment_list'),
    path('create/', AudioCommentCreateView.as_view(), name='audio_comment_create'),
]