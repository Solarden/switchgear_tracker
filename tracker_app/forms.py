from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

from tracker_app.models import Worker, Company, Switchgear, SwitchgearComponents, SwitchgearParameters, Client, Order, \
    Component, SwitchgearPhotos


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
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź nazwę użytkownika'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź adres email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź imię'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź nazwisko'}),
        }
        help_texts = {
            'username': None,
        }


class AdminWorkerChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = Worker
        fields = ('groups',)
        widgets = {
            'groups': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class WorkerPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Wprowadź bieżące hasło', 'type': 'password', }))
    new_password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Wprowadź nowe hasło', 'type': 'password', }))
    new_password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Powtórz nowe hasło', 'type': 'password', }))

    class Meta:
        model = Worker
        fields = ('old_password', 'new_password1', 'new_password2')


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
            'logo': 'Wybierz zdjęcie'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź nazwę firmy'}),
            'owner': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź dane właściciela'}),
            'nip': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź numer NIP'}),
            'hq': forms.Textarea(
                attrs={'class': 'form-control', 'rows': '2', 'placeholder': 'Wprowadź adres siedziby firmy'}),
            'prod': forms.Textarea(
                attrs={'class': 'form-control', 'rows': '2',
                       'placeholder': 'Wprowadź adres zakładu produkcyjnego firmy'}),
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
            'ready_to_ship': 'Gotowa do wysyłki',
            'req_shipment': 'Żądana data dostawy',
            'actual_shipment': 'Rzeczywista data wysyłki',
            'made_by': 'Wykonany przez',
        }
        widgets = {
            'order_ref': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź nazwę rozdzielni'}),
            'serial_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź numer zamówienia'}),
            'switchgear_parameters': forms.Select(attrs={'class': 'form-control'}),
            'shipped': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ready_to_ship': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'req_shipment': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Wprowadź datę dostarczenia'}),
            'actual_shipment': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Wprowadź datę wysyłki'}),
            'made_by': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'stuff_missing': forms.HiddenInput(),
            'has_photos': forms.HiddenInput(),
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
            'amount_needed': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Wprowadź wymaganą ilość'}),
            'amount_missing': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Wprowadź brakującą ilość'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź numer seryjny'}),
            'supplier': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź nazwę dostawcy'}),
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
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź nazwę charakterystyki'}),
            'par_a': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź prąd znamionowy'}),
            'par_ka': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź prąd zwarciowy'}),
            'par_v': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź napięcie znamionowe'}),
            'par_ui': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Wprowadź napięcie wytrzymywane'}),
            'par_hz': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Wprowadź częstotliwość znamionową'}),
            'par_grid': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź typ sieci'}),
            'par_protection': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Wprowadź klasę ochronności'}),
            'par_ip': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź klasę IP'}),
            'par_ik': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź klasyfikacje IK'}),
        }


class ClientModelForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        labels = {
            'name': 'Nazwa klienta',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź nazwę klienta'}),
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
            'order_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź nazwę zamówienia'}),
            'ordered_by': forms.Select(attrs={'class': 'form-control'}),
            'added_by': forms.HiddenInput(attrs={'class': 'form-control'}),
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
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź nazwę komponentu'}),
            'producer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź nazwę producenta'}),
            'catalogue_number': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Wprowadź numer katalogowy'}),
        }


class SwitchgearPhotosModelForm(forms.ModelForm):
    class Meta:
        model = SwitchgearPhotos
        fields = '__all__'
        labels = {
            'ref_switchgear': 'Nazwa rozdzielni',
            'photo': 'Zdjęcie rozdzielni',
        }
        widgets = {
            'ref_switchgear': forms.Select(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'label': 'Wybierz zdjęcie'})
        }
