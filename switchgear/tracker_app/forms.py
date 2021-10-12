from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from tracker_app.models import Worker


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class WorkerCreationForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = ('username', 'email')


class WorkerChangeForm(UserChangeForm):
    class Meta:
        model = Worker
        fields = ('username', 'email')
