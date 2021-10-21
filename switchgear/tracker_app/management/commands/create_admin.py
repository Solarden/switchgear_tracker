from django.contrib.auth.models import Group
from django.core.management import BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from tracker_app.models import Worker


class Command(BaseCommand):
    help = 'Creates first admin account for an app'

    def handle(self, *args, **options):
        while True:
            admin_username = input('Podaj nazwę użytkownika: ')
            try:
                Worker.objects.get(username=admin_username)
                print('Konto o tej nazwie już istnieje! Wybierz inną!')
            except ObjectDoesNotExist:
                admin_password1 = input('Podaj hasło użytkownika: ')
                admin_password2 = input('Powtórz hasło użytkownika: ')
                if admin_password1 != admin_password2:
                    print('Hasła różnią się od siebie!')
                else:
                    Worker.objects.create_user(username=admin_username, password=admin_password1)
                    admin = Worker.objects.get(username=admin_username)
                    admin_group = Group.objects.get(id=1)
                    admin.groups.add(admin_group)
                    print('Konto zostało utworzone')
                    break
