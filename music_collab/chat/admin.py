from django.contrib import admin
from .models import Chat, Message

class MessageInline(admin.TabularInline):
    model = Message
    extra = 1  # Количество пустых форм для добавления новых сообщений

class ChatAdmin(admin.ModelAdmin):
    inlines = [MessageInline]

admin.site.register(Chat, ChatAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('chat', 'sender', 'content', 'created_at')
    list_filter = ('chat', 'sender', 'message_type')
    search_fields = ('content',)

admin.site.register(Message, MessageAdmin)