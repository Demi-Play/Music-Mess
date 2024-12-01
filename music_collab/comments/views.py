from django.shortcuts import render, redirect
from django.views import View
from .models import AudioComment
from .forms import AudioCommentForm

class AudioCommentListView(View):
    def get(self, request):
        comments = AudioComment.objects.all()
        return render(request, 'comments/audio_comment_list.html', {'comments': comments})

class AudioCommentCreateView(View):
    def get(self, request):
        form = AudioCommentForm()
        return render(request, 'comments/audio_comment_form.html', {'form': form})

    def post(self, request):
        form = AudioCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user  # Устанавливаем текущего пользователя как автора комментария
            comment.save()
            return redirect('comments:audio_comment_list')
        return render(request, 'comments/audio_comment_form.html', {'form': form})