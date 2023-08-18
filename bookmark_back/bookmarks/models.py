from django.conf import settings
from django.db import models


class Bookmark(models.Model):
    LINK_TYPES = (
        ('website', 'Website'),
        ('book', 'Book'),
        ('article', 'Article'),
        ('music', 'Music'),
        ('video', 'Video'),
    )

    title = models.CharField(max_length=255, verbose_name='Заголовок страницы')
    description = models.TextField(blank=True, null=True, verbose_name='Краткое описание')
    url = models.URLField(verbose_name='Ссылка на страницу')
    link_type = models.CharField(max_length=7, choices=LINK_TYPES, default='website', verbose_name='Тип ссылки')
    og_image = models.URLField(blank=True, null=True, verbose_name='Картинка превью')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
