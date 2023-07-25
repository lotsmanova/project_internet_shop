from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Product(models.Model):
    name = models.CharField(max_length=150,  verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='product/', verbose_name='изображение', **NULLABLE)
    category = models.ImageField()
    price = models.PositiveIntegerField(verbose_name='цена')
    date_create = models.DateField(verbose_name='дата создания', **NULLABLE)
    date_change = models.DateField(verbose_name='дата последнего изменения', **NULLABLE)


class Category(models.Model):
    pass