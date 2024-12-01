from django.contrib import admin
from .models import AudioComment

class AudioCommentAdmin(admin.ModelAdmin):
    list_display = ('file', 'user', 'timestamp', 'text', 'created_at')
    list_filter = ('file',)
    search_fields = ('text',)

admin.site.register(AudioComment, AudioCommentAdmin)