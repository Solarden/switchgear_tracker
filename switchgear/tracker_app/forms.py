from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from tracker_app.models import Worker, Company, Switchgear, SwitchgearComponents, SwitchgearParameters, Client, Order, \
    Component


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
            'switchgear_parameters': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'shipped': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ready_to_ship': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'req_shipment': forms.DateInput(attrs={'class': 'form-control'}),
            'actual_shipment': forms.DateInput(attrs={'class': 'form-control'}),
            'made_by': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class SwitchgearComponentsModelForm(forms.ModelForm):
    class Meta:
        model = SwitchgearComponents
        fields = '__all__'
        labels = {
            'component': 'Komponent',
            'switchgear': 'Rozdzielnia',
            'amount_needed': 'Potrzebna ilość',
            'amount_missing': 'Brakująca ilość',
            'serial_number': 'Numer fabryczny',
            'supplier': 'Dostawca',
        }
        widgets = {
            'component': forms.Select(attrs={'class': 'form-control'}),
            'switchgear': forms.Select(attrs={'class': 'form-control'}),
            'amount_needed': forms.NumberInput(attrs={'class': 'form-control'}),
            'amount_missing': forms.NumberInput(attrs={'class': 'form-control'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control'}),
            'supplier': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SwitchgearParametersModelForm(forms.ModelForm):
    class Meta:
        model = SwitchgearParameters
        fields = '__all__'
        labels = {
            'name': 'Nazwa charakterystyki',
            'par_a': 'Prąd znamionowy (A)',
            'par_ka': 'Prąd zwarciowy (kA)',
            'par_v': 'Napięcie znamionowe (V)',
            'par_ui': 'Napięcie wytrzymywane (Ul)',
            'par_hz': 'Częstotliwość znamionowa (Hz)',
            'par_grid': 'Typ sieci',
            'par_protection': 'Klasa ochronności',
            'par_ip': 'Klasa ochronności IP',
            'par_ik': 'Klasyfikacja (udary mechaniczne) IK',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'par_a': forms.NumberInput(attrs={'class': 'form-control'}),
            'par_ka': forms.NumberInput(attrs={'class': 'form-control'}),
            'par_v': forms.NumberInput(attrs={'class': 'form-control'}),
            'par_ui': forms.NumberInput(attrs={'class': 'form-control'}),
            'par_hz': forms.TextInput(attrs={'class': 'form-control'}),
            'par_grid': forms.TextInput(attrs={'class': 'form-control'}),
            'par_protection': forms.NumberInput(attrs={'class': 'form-control'}),
            'par_ip': forms.NumberInput(attrs={'class': 'form-control'}),
            'par_ik': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ClientModelForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        labels = {
            'name': 'Nazwa klienta',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        labels = {
            'order_name': 'Nazwa zamówienia',
            'ordered_by': 'Klient',
            'added_by': 'Dodający zamówienie',
        }
        widgets = {
            'order_name': forms.TextInput(attrs={'class': 'form-control'}),
            'ordered_by': forms.Select(attrs={'class': 'form-control'}),
            'added_by': forms.Select(attrs={'class': 'form-control'}),
        }


class ComponentModelForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = '__all__'
        labels = {
            'name': 'Nazwa komponentu',
            'producer': 'Producent',
            'catalogue_number': 'Numer katalogowy',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'producer': forms.TextInput(attrs={'class': 'form-control'}),
            'catalogue_number': forms.TextInput(attrs={'class': 'form-control'}),
        }
