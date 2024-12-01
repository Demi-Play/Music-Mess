from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'assignee', 'status', 'due_date')
    list_filter = ('status', 'project')
    search_fields = ('title', 'description')

admin.site.register(Task, TaskAdmin)