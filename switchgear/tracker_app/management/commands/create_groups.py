from django.core.management import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission


class Command(BaseCommand):
    help = 'Creates permission groups for users'

    def handle(self, *args, **options):
        print('Creating admin group')
        group_admin = Group.objects.get_or_create(name='admin')
        for i in range(20, 57):
            p = Permission.objects.get(id=i)
            group_admin[0].permissions.add(p)
        print('Creating biuro group')
        group_biuro = Group.objects.get_or_create(name='biuro')
        for i in range(20, 25):
            p = Permission.objects.get(id=i)
            group_biuro[0].permissions.add(p)
        p26 = Permission.objects.get(id=26)
        group_biuro[0].permissions.add(p26)
        for i in range(28, 45):
            p = Permission.objects.get(id=i)
            group_biuro[0].permissions.add(p)
        for i in range(49, 57):
            p = Permission.objects.get(id=i)
            group_biuro[0].permissions.add(p)
        print('Creating prod group')
        group_prod = Group.objects.get_or_create(name='prod')
        p24 = Permission.objects.get(id=24)
        p28 = Permission.objects.get(id=28)
        p29 = Permission.objects.get(id=29)
        p30 = Permission.objects.get(id=30)
        p32 = Permission.objects.get(id=32)
        p36 = Permission.objects.get(id=36)
        p37 = Permission.objects.get(id=37)
        p44 = Permission.objects.get(id=44)
        p49 = Permission.objects.get(id=49)
        p50 = Permission.objects.get(id=50)
        p52 = Permission.objects.get(id=52)
        p53 = Permission.objects.get(id=53)
        p56 = Permission.objects.get(id=56)
        group_prod[0].permissions.add(p24, p28, p29, p30, p32, p36, p37, p44, p49, p50, p52, p53, p56)
        print('Groups configured')
