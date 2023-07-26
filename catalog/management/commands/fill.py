from django.core.management import BaseCommand, call_command

from catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        # удаление данных
        Product.objects.all().delete()
        # добавление данных
        call_command('loaddata', 'catalog_data.json')