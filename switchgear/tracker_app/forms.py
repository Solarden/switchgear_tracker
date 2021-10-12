from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from tracker_app.models import Worker, Company, Switchgear


class WorkerCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = Worker
        fields = ('username', 'email', 'first_name', 'last_name')


class WorkerChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = Worker
        fields = ('username', 'email', 'first_name', 'last_name')
        labels = {
            'username': 'Nazwa użytkownika',
            'email': 'Adres email',
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'username': None,
        }


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
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'owner': forms.TextInput(attrs={'class': 'form-control'}),
            'nip': forms.TextInput(attrs={'class': 'form-control'}),
            'hq': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
            'prod': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
        }


class SwitchgearModelForm(forms.ModelForm):
    class Meta:
        model = Switchgear
        exclude = ('components',)
        labels = {
            'order_ref': 'Numer zamówienia',
            'name': 'Nazwa rozdzielni',
            'serial_no': 'Numer seryjny',
            'switchgear_parameters': 'Charakterystyka rozdzielni',
            'shipped': 'Status wysyłki',
            'ready_to_ship': 'Gotowy do wysyłki',
            'req_shipment': 'Żądana data dostawy',
            'actual_shipment': 'Rzeczywista data wysyłki',
            'made_by': 'Wykonany przez',
        }
        widgets = {
            'order_ref': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_no': forms.TextInput(attrs={'class': 'form-control'}),
            'switchgear_parameters': forms.Select(attrs={'class': 'form-control'}),
            'shipped': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ready_to_ship': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'req_shipment': forms.DateInput(attrs={'class': 'form-control'}),
            'actual_shipment': forms.DateInput(attrs={'class': 'form-control'}),
            'made_by': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
