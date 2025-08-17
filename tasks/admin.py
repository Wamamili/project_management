from django.contrib import admin
from .models import Task, Comment

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'project', 'assigned_to', 'status', 'priority', 'due_date', 'created_by')
    list_filter = ('status', 'priority', 'due_date', 'project')
    search_fields = ('title', 'description')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'author', 'timestamp')
    search_fields = ('task__title', 'author__username', 'body')
