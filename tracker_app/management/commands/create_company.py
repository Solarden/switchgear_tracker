from django.core.exceptions import ObjectDoesNotExist
from django.core.management import BaseCommand
from tracker_app.models import Company


class Command(BaseCommand):
    help = 'Creates first company for app'

    def handle(self, *args, **options):
        try:
            Company.objects.get(id=1)
            print('Company already exists!')
        except ObjectDoesNotExist:
            Company.objects.create(name='Firma przykładowa', owner='Brajanusz Konieczko', nip='1234567890',
                                   hq='Izraelska 21/37, 02-676 Warszawa', prod='Izraelska 21/37, 02-676 Warszawa')
            print('Company created!')
