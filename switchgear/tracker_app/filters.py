import django_filters
from django import forms
from django_filters import CharFilter

from .models import Switchgear


class SwitchgearFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label="Nazwa rozdzielni:",
                      widget=forms.TextInput(
                          attrs={'class': 'form-control', 'placeholder': 'Wprowadź nazwę rozdzielni'}))
    serial_no = CharFilter(field_name='serial_no', lookup_expr='icontains', label="Numer fabryczny:",
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'Wprowadź numer fabryczny'}))

    class Meta:
        model = Switchgear
        fields = ('name', 'serial_no')
