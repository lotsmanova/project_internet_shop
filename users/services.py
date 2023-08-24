import random

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from users.tokens import account_activation_token


def register_send_mail(new_user, current_site):
    mail_subject = 'Активация аккаунта'
    message = render_to_string('users/activation_email.html', {
        'user': new_user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
        'token': account_activation_token.make_token(new_user),
    })

    send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [new_user.email])


def generate_new_password(request):
    """Контроллер генерации нового пароля"""

    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])

    send_mail(
        'Смена пароля',
        f'Ваш новый пароль "{new_password}"',
        settings.EMAIL_HOST_USER,
        [request.user.email],
        fail_silently=False,
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('catalog:home_page'))