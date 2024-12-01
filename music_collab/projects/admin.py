from django.contrib import admin
from .models import Project, JoinRequest

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at', 'status')
    list_filter = ('status',)
    search_fields = ('name', 'description')

admin.site.register(Project, ProjectAdmin)

class JoinRequestAdmin(admin.ModelAdmin):
    list_display = ['project', 'user', 'confirmed']
    list_filter = ('project',)
    search_fields = ('project', 'user')

admin.site.register(JoinRequest, JoinRequestAdmin)