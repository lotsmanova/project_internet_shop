from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@fox.ru',
            first_name='Admin',
            last_name='Fox',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('159asd753qwe')
        user.save()
