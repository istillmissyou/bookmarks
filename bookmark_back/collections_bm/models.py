from django.db import models

from bookmarks.models import Bookmark


class Collection(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Краткое описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    updated_at = models.DateTimeField('Дата и время изменения', auto_now=True)
    bookmarks = models.ManyToManyField(Bookmark, related_name='collections')

    def __str__(self):
        return self.name
