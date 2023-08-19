from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(verbose_name='email', unique=True)

    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=50, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='страна', **NULLABLE)
    is_active = models.BooleanField(verbose_name='статус активности', default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

