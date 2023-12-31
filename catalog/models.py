from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='product/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.PositiveIntegerField(verbose_name='цена')
    date_create = models.DateField(verbose_name='дата создания', **NULLABLE)
    date_change = models.DateField(verbose_name='дата последнего изменения', **NULLABLE)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='пользователь', **NULLABLE)


    @property
    def active_version(self):
        return self.version_set.filter(is_active=True).first()


    def __str__(self):
        return f'{self.name} ({self.category})'


    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    num = models.PositiveIntegerField(verbose_name='номер версии')
    name = models.CharField(max_length=150, verbose_name='название версии')
    is_active = models.BooleanField(verbose_name='признак')


    def __str__(self):
        return f'{self.name} - {self.num}'


    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'


class Contact(models.Model):
    name = models.CharField(max_length=150, verbose_name='компания')
    email = models.EmailField(verbose_name='email')
    phone = models.CharField(max_length=50, verbose_name='телефон')
    address = models.CharField(max_length=150, verbose_name='адрес')


    def __str__(self):
        return f'{self.name} ({self.address})'


    class Meta:
        verbose_name = 'контакты'
        verbose_name_plural = 'контакты'



