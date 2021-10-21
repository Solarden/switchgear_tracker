from django.core.management import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission


class Command(BaseCommand):
    help = 'Creates read only default permission groups for users'

    def handle(self, *args, **options):
        group_test = Group.objects.get(name='group_test')
        p25 = Permission.objects.get(codename='view_worker')
        group_test.permissions.add(p25)
