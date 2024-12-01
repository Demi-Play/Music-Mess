from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Chat, Message
from .forms import MessageForm, ChatForm
from projects.models import Project
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class ChatListView(View):
    def get(self, request):
        chats = Chat.objects.all()
        return render(request, 'chat/chat_list.html', {'chats': chats})
    
@method_decorator(login_required, name='dispatch')
class ChatCreateView(View):
    def get(self, request):
        form = ChatForm()
        projects = Project.objects.all()  # Получаем все проекты для выбора
        return render(request, 'chat/chat_form.html', {'form': form, 'projects': projects})

    def post(self, request):
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = form.save(commit=False)
            project_id = request.POST.get('project')  # Получаем ID проекта из формы
            chat.project = Project.objects.get(id=project_id)  # Получаем экземпляр проекта
            chat.save()
            return redirect('chat:chat_list')
        projects = Project.objects.all()  # Получаем проекты для повторного отображения формы
        return render(request, 'chat/chat_form.html', {'form': form, 'projects': projects})

@method_decorator(login_required, name='dispatch')
class ChatDetailView(View):
    def get(self, request, pk):
        chat = get_object_or_404(Chat, pk=pk)
        messages = chat.messages.all()
        return render(request, 'chat/chat_detail.html', {'chat': chat, 'messages': messages})

    def post(self, request, pk):
        chat = get_object_or_404(Chat, pk=pk)
        
        # Получаем тип сообщения из кнопки
        if request.POST.get('content'):
            message_type = 'text'
            content = request.POST['content']
        elif request.POST.get('video_call'):
            message_type = 'video_call'
            content = "Видеозвонок начат."
        elif request.POST.get('voice_call'):
            message_type = 'call'
            content = "Звонок начат."

        # Создаем новое сообщение
        message = Message(chat=chat, sender=request.user, content=content, message_type=message_type)
        message.save()
        
        return redirect('chat:chat_detail', pk=pk)