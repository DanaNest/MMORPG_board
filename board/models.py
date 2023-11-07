from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField


# class User(models.Model):
#     email = models.EmailField(unique=True)
#     is_active = models.BooleanField(default=False)
#     activation_code = models.CharField(max_length=20, blank=True, null=True)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    LIST_CHOICE = [
        ('Tanks', 'Танки'),
        ('Healers', 'Хилы'),
        ('DD', 'ДД'),
        ('Traders', 'Торговцы'),
        ('GM', 'Гилдмастеры'),
        ('QG', 'Квестгиверы'),
        ('Smiths', 'Кузнецы'),
        ('Leatherworkers', 'Кожевники'),
        ('Potions', 'Зельленары'),
        ('Spell', 'Мастера заклинаний')
    ]
    category = models.CharField(max_length=18, choices=LIST_CHOICE, verbose_name='Категория')
    title = models.CharField(max_length=256, verbose_name='Название')
    content2 = RichTextUploadingField(config_name='special',
        # extra_plugins=['youtube'],
        # external_plugin_resources=[(
        #     'youtube',
        #     '/static/ckeditor/ckeditor/plugins/youtube/',
        #     'plugin.js',
        #
        # )],
        null=True,
    )
    content = RichTextUploadingField(verbose_name='Текст')
    data_creation = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.title


class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replies', verbose_name='Пост')
    text = models.TextField(verbose_name='Текст')
    status = models.BooleanField(default=False)
