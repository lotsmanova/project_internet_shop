import random
from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView, PasswordResetView, PasswordResetConfirmView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import CreateView, TemplateView, UpdateView
from users.forms import UserRegisterForm, UserForm, UserFormPasswordForm, UserSetNewPasswordForm
from users.models import User
from users.tokens import account_activation_token


class LoginView(BaseLoginView):
    """Контроллер входа в аккаунт"""

    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    """Контроллер выхода из аккаунта"""

    pass


class RegisterView(CreateView):
    """Контроллер регистрации пользователя"""

    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.is_active = False
        new_user.save()

        current_site = get_current_site(self.request)
        mail_subject = 'Активация аккаунта'
        message = render_to_string('users/activation_email.html', {
            'user': new_user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
            'token': account_activation_token.make_token(new_user),
        })

        send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [new_user.email])
        return super().form_valid(form)


class UserActivateView(TemplateView):
    """Контроллер верификации аккаунта"""

    template_name = 'users/activate.html'

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return self.render_to_response({'activated': True})

        return self.render_to_response({'activated': False})


class UserProfileView(UpdateView):
    """Контроллер профиля пользователя"""

    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


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


class UserForgotPasswordView(SuccessMessageMixin, PasswordResetView):
    """Контроллер для сброса пароля"""

    form_class = UserFormPasswordForm
    template_name = 'users/password_reset.html'
    success_url = reverse_lazy('catalog:home_page')
    success_message = 'Письмо с инструкцией по восстановлению пароля отправлена на ваш email'
    subject_template_name = 'users/email/password_reset_subject.txt'
    email_template_name = 'users/email/password_reset_mail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Запрос на восстановление пароля'
        return context


class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    """Контроллер создания нового пароля"""

    form_class = UserSetNewPasswordForm
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('catalog:home_page')
    success_message = 'Пароль успешно изменен. Можете авторизоваться на сайте.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Установить новый пароль'
        return context
