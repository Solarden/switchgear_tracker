from django.contrib.auth.models import AbstractUser
from django.db import models


class Company(models.Model):
    login = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)
    company_name = models.CharField(max_length=128, unique=True)
    company_owner = models.CharField(max_length=64)
    company_hq = models.TextField()
    company_prod = models.TextField()
    company_logo = models.FileField()


class Worker(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Client(models.Model):
    name = models.CharField(max_length=128, unique=True)


class Order(models.Model):
    order_name = models.CharField(max_length=64)
    ordered_by = models.ForeignKey(Client, on_delete=models.PROTECT)
    added_by = models.ForeignKey(Worker, on_delete=models.PROTECT)


class SwitchgearParameters(models.Model):
    name = models.CharField(max_length=64)
    par_a = models.IntegerField()
    par_ka = models.IntegerField()
    par_v = models.IntegerField()
    par_ui = models.IntegerField()
    par_hz = models.IntegerField()
    par_grid = models.CharField(max_length=8)
    par_protection = models.IntegerField()
    par_ip = models.IntegerField()
    par_ik = models.IntegerField()


class Switchgear(models.Model):
    order_ref = models.ForeignKey(Order, on_delete=models.PROTECT)
    name = models.CharField(max_length=64)
    serial_no = models.CharField(max_length=32)
    switchgear_parameters = models.ManyToManyField(SwitchgearParameters)
    shipped = models.BooleanField(default=False)
    ready_to_ship = models.BooleanField(default=False)
    req_shipment = models.DateField()
    actual_shipment = models.DateField()
    made_by = models.ManyToManyField(Worker)
    components = models.ManyToManyField('Component', through='SwitchgearComponents')


class Component(models.Model):
    name = models.CharField(max_length=255)
    producer = models.CharField(max_length=64)
    catalogue_number = models.CharField(max_length=64)


class SwitchgearComponents(models.Model):
    component = models.ForeignKey(Component, on_delete=models.PROTECT)
    switchgear = models.ForeignKey(Switchgear, on_delete=models.PROTECT)
    amount_needed = models.IntegerField()
    amount_missing = models.IntegerField()
    serial_number = models.CharField(max_length=64)
    supplier = models.CharField(max_length=64)
