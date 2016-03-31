from django.contrib import admin
from .models import Task, File_storage

class File_storageInline(admin.TabularInline):
    model = File_storage


@admin.register(Task)
class TasksAdmin(admin.ModelAdmin):
    inlines = [
        File_storageInline,
    ]