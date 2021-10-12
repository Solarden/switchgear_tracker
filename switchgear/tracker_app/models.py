from django.contrib.auth.models import AbstractUser
from django.core.files.storage import FileSystemStorage
from django.db import models

fs_logo = FileSystemStorage(location='media/logos/')


class Company(models.Model):
    name = models.CharField(max_length=128, unique=True)
    owner = models.CharField(max_length=64)
    nip = models.CharField(max_length=13)
    hq = models.TextField()
    prod = models.TextField()
    logo = models.FileField(storage=fs_logo)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Client(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_name = models.CharField(max_length=64)
    ordered_by = models.ForeignKey(Client, on_delete=models.PROTECT)
    added_by = models.ForeignKey(Worker, on_delete=models.PROTECT)

    def __str__(self):
        return self.order_name


class SwitchgearParameters(models.Model):
    name = models.CharField(max_length=64)
    par_a = models.IntegerField()
    par_ka = models.IntegerField()
    par_v = models.IntegerField()
    par_ui = models.IntegerField()
    par_hz = models.CharField(max_length=16)
    par_grid = models.CharField(max_length=8)
    par_protection = models.IntegerField()
    par_ip = models.IntegerField()
    par_ik = models.IntegerField()

    def __str__(self):
        return self.name


class Switchgear(models.Model):
    order_ref = models.ForeignKey(Order, on_delete=models.PROTECT)
    name = models.CharField(max_length=64)
    serial_no = models.CharField(max_length=32)
    switchgear_parameters = models.ManyToManyField(SwitchgearParameters)
    shipped = models.BooleanField(default=False)
    ready_to_ship = models.BooleanField(default=False)
    req_shipment = models.DateField(null=True, blank=True)
    actual_shipment = models.DateField(null=True, blank=True)
    made_by = models.ManyToManyField(Worker)
    components = models.ManyToManyField('Component', through='SwitchgearComponents')

    def __str__(self):
        return self.name


class Component(models.Model):
    name = models.CharField(max_length=255)
    producer = models.CharField(max_length=64)
    catalogue_number = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class SwitchgearComponents(models.Model):
    component = models.ForeignKey(Component, on_delete=models.PROTECT)
    switchgear = models.ForeignKey(Switchgear, on_delete=models.PROTECT)
    amount_needed = models.IntegerField()
    amount_missing = models.IntegerField()
    serial_number = models.CharField(max_length=64, blank=True, null=True)
    supplier = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.component.name
