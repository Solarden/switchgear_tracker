import django_filters
from django import forms
from django_filters import CharFilter, ChoiceFilter, ModelChoiceFilter

from .models import Switchgear, Worker, SwitchgearComponents, Component, SwitchgearParameters, Client

SHIPPED_CHOICES = ((0, 'Nie'), (1, 'Tak'))


class SwitchgearFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label="Nazwa rozdzielni:",
                      widget=forms.TextInput(
                          attrs={'class': 'form-control', 'placeholder': 'Wprowadź nazwę rozdzielni'}))
    serial_no = CharFilter(field_name='serial_no', lookup_expr='icontains', label="Numer fabryczny:",
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'Wprowadź numer fabryczny'}))
    shipped = ChoiceFilter(field_name='shipped', label='Wysłana:', choices=SHIPPED_CHOICES,
                           widget=forms.Select(attrs={'class': 'form-control'}))
    made_by = ModelChoiceFilter(field_name='made_by', label='Wykonana przez:', queryset=Worker.objects.all(),
                                widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Switchgear
        fields = ('name', 'serial_no', 'shipped', 'made_by')


class SwitchgearComponentsFilter(django_filters.FilterSet):
    name = CharFilter(field_name='component__name', lookup_expr='icontains', label="Nazwa rozdzielni:",
                      widget=forms.TextInput(
                          attrs={'class': 'form-control', 'placeholder': 'Wprowadź nazwę komponentu'}))
    catalogue_number = CharFilter(field_name='component__catalogue_number', lookup_expr='icontains',
                                  label="Nazwa rozdzielni:",
                                  widget=forms.TextInput(
                                      attrs={'class': 'form-control', 'placeholder': 'Wprowadź numer katalogowy'}))

    class Meta:
        model = SwitchgearComponents
        fields = ('name', 'catalogue_number')


class SwitchgearParametersFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label="Nazwa charakterystyki:",
                      widget=forms.TextInput(
                          attrs={'class': 'form-control', 'placeholder': 'Wprowadź nazwę charakterystyki'}))

    class Meta:
        model = SwitchgearParameters
        fields = ('name',)


class ClientFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label="Nazwa klienta:",
                      widget=forms.TextInput(
                          attrs={'class': 'form-control', 'placeholder': 'Wprowadź nazwę klienta'}))

    class Meta:
        model = Client
        fields = ('name',)


class OrderFilter(django_filters.FilterSet):
    order_name = CharFilter(field_name='order_name', lookup_expr='icontains', label="Nazwa zamówienia:",
                            widget=forms.TextInput(
                                attrs={'class': 'form-control', 'placeholder': 'Wprowadź nazwę zamówienia'}))
    ordered_by = CharFilter(field_name='ordered_by__name', lookup_expr='icontains', label="Nazwa klienta:",
                            widget=forms.TextInput(
                                attrs={'class': 'form-control', 'placeholder': 'Wprowadź nazwę klienta'}))

    class Meta:
        model = Client
        fields = ('order_name', 'ordered_by')


class ComponentFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label="Nazwa komponentu:",
                      widget=forms.TextInput(
                          attrs={'class': 'form-control', 'placeholder': 'Wprowadź nazwę komponentu'}))
    catalogue_number = CharFilter(field_name='catalogue_number', lookup_expr='icontains', label="Numer katalogowy:",
                                  widget=forms.TextInput(
                                      attrs={'class': 'form-control', 'placeholder': 'Wprowadź numer katalogowy'}))

    class Meta:
        model = Component
        fields = ('name', 'catalogue_number')
