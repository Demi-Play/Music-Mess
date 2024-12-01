from django.contrib import admin
from .models import File

class FileAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_by', 'file_type', 'uploaded_at')
    list_filter = ('file_type',)
    search_fields = ('file',)

admin.site.register(File, FileAdmin)