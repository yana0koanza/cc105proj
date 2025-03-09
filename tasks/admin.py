from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'status')  # Include status in the list
    list_filter = ('status',)
