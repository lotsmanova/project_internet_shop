from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Category(models.Model):
    name = models.CharField(max_length=150,  verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=150,  verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='product/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.PositiveIntegerField(verbose_name='цена')
    date_create = models.DateField(verbose_name='дата создания', **NULLABLE)
    date_change = models.DateField(verbose_name='дата последнего изменения', **NULLABLE)
    created_at = models.BooleanField(verbose_name='создан')

    def __str__(self):
        return f'{self.name} ({self.category})'


    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'