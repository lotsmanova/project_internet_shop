from django.db import models

from catalog.models import NULLABLE


class Blog(models.Model):
    head = models.CharField(max_length=200, verbose_name='заголовок')
    slug = models.CharField(max_length=200, verbose_name='slug')
    body = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog/', verbose_name='превью', **NULLABLE)
    date_create = models.DateField(verbose_name='дата создания', **NULLABLE)
    is_public = models.BooleanField(default=True, verbose_name='опубликовано')
    count_views = models.PositiveIntegerField(default=0, verbose_name='количество просмотров')


    def __str__(self):
        return f'{self.head} ({self.slug})'


    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
