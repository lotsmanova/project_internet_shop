from django.db import models
from django.utils.text import slugify

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


    def __str__(self):
        return f'{self.name} ({self.category})'


    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


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

class Blog(models.Model):
    head = models.CharField(max_length=200, verbose_name='заголовок')
    slug = models.CharField(max_length=200, verbose_name='slug')
    body = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog/', verbose_name='превью', **NULLABLE)
    date_create = models.DateField(verbose_name='дата создания', **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name='опубликован')
    count_views = models.PositiveIntegerField(default=0, verbose_name='количество просмотров')


    def save(self, *args, **kwargs):
        self.slug = slugify(self.head)
        super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.head} ({self.slug})'


    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
