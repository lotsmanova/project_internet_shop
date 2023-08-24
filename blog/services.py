from django.conf import settings
from django.core.mail import send_mail

from blog.models import Blog


def blog_send_mail(object):
    send_mail(
        'Поздравляем!',
        f'Ваша статья "{object.head}" набрала 100 просмотров!',
        settings.EMAIL_HOST_USER,
        ['lotsmanovavioletta@yandex.ru'],
        fail_silently=False,
    )