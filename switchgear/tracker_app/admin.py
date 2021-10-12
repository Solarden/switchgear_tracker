from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tracker_app import models

# Register your models here.
from tracker_app.forms import WorkerCreationForm, WorkerChangeForm
from tracker_app.models import Worker


class CustomUserAdmin(UserAdmin):
    add_form = WorkerCreationForm
    form = WorkerChangeForm
    model = Worker
    list_display = ['email', 'username', ]


admin.site.register(Worker, CustomUserAdmin)
