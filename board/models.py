from django.db import models
from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    LIST_CHOICE = [
        ('Tanks', 'Танки'),
        ('Healers', 'Хилы'),
        ('DD', 'ДД'),
        ('Traders', 'Торговцы'),
        ('GM', 'Гилдмастеры'),
        ('QG', 'Квестгиверы'),
        ('Smiths', 'Кузнецы'),
        ('Leatherworkers', 'Кожевники'),
        ('Potions', 'Зельевары'),
        ('Spell', 'Мастера заклинаний')
    ]
    category = models.CharField(max_length=18, choices=LIST_CHOICE, verbose_name='Категория')
    title = models.CharField(max_length=256, verbose_name='Название')
    content = RichTextUploadingField(config_name='special', verbose_name='Текст', null=True)
    data_creation = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            self.author = self.request.user
        super().save(*args, **kwargs)


class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replies', verbose_name='Пост')
    data_creation = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    text = models.TextField(verbose_name='Текст')
    status = models.BooleanField(default=False)


