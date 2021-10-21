from django.core.management import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission


class Command(BaseCommand):
    help = 'Creates read only default permission groups for users'

    def handle(self, *args, **options):
        print('Creating admin group')
        group_admin = Group.objects.get_or_create(name='admin')
        for i in range(25, 61):
            p = Permission.objects.get(id=i)
            group_admin[0].permissions.add(p)
        print('Creating biuro group')
        group_biuro = Group.objects.get_or_create(name='biuro')
        for i in range(25, 37):
            p = Permission.objects.get(id=i)
            group_biuro[0].permissions.add(p)
        for i in range(41, 49):
            p = Permission.objects.get(id=i)
            group_biuro[0].permissions.add(p)
        p50 = Permission.objects.get(id=50)
        group_biuro[0].permissions.add(p50)
        for i in range(52, 58):
            p = Permission.objects.get(id=i)
            group_biuro[0].permissions.add(p)
        p59 = Permission.objects.get(id=59)
        p60 = Permission.objects.get(id=60)
        group_biuro[0].permissions.add(p59, p60)
        print('Creating prod group')
        group_prod = Group.objects.get_or_create(name='prod')
        p28 = Permission.objects.get(id=28)
        p32 = Permission.objects.get(id=32)
        p33 = Permission.objects.get(id=33)
        p34 = Permission.objects.get(id=34)
        p36 = Permission.objects.get(id=36)
        p44 = Permission.objects.get(id=44)
        p48 = Permission.objects.get(id=48)
        p52 = Permission.objects.get(id=52)
        p53 = Permission.objects.get(id=53)
        p54 = Permission.objects.get(id=54)
        p56 = Permission.objects.get(id=56)
        p57 = Permission.objects.get(id=57)
        group_prod[0].permissions.add(p28, p32, p33, p34, p36, p44, p48, p52, p53, p54, p56, p57, p60)
        print('Groups configured')
