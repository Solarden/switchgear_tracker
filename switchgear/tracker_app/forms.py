from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from tracker_app.models import Worker, Company


class WorkerCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = Worker
        fields = ('username', 'email', 'first_name', 'last_name')


class WorkerChangeForm(UserChangeForm):
    class Meta:
        model = Worker
        fields = ('username', 'email')


class CompanyModelForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        labels = {
            'name': 'Nazwa firmy',
            'owner': 'Właściciel',
            'nip': 'Numer NIP',
            'hq': 'Adres firmy',
            'prod': 'Adres produkcji',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control md-5'}),
            'owner': forms.TextInput(attrs={'class': 'form-control'}),
            'nip': forms.TextInput(attrs={'class': 'form-control'}),
            'hq': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
            'prod': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
        }
