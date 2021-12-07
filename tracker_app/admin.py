from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tracker_app.forms import WorkerCreationForm, WorkerChangeForm
from tracker_app.models import Worker, Company, Switchgear, Client, SwitchgearComponents, Component, \
    SwitchgearParameters, Order, SwitchgearPhotos


class CustomUserAdmin(UserAdmin):
    add_form = WorkerCreationForm
    form = WorkerChangeForm
    model = Worker
    list_display = ['email', 'username', ]


admin.site.register(Worker, CustomUserAdmin)
admin.site.register(Company)
admin.site.register(Switchgear)
admin.site.register(Client)
admin.site.register(SwitchgearComponents)
admin.site.register(Component)
admin.site.register(SwitchgearParameters)
admin.site.register(Order)
admin.site.register(SwitchgearPhotos)
