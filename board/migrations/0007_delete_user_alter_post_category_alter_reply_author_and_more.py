# Generated by Django 4.2.7 on 2023-11-06 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0006_rename_author_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Tanks', 'Танки'), ('Healers', 'Хилы'), ('DD', 'ДД'), ('Traders', 'Торговцы'), ('GM', 'Гилдмастеры'), ('QG', 'Квестгиверы'), ('Кузнецы', 'Кузнецы'), ('Leatherworkers', 'Кожевники'), ('Potions', 'Зельевары'), ('Spell', 'Мастера заклинаний')], max_length=15, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='board.post', verbose_name='Пост'),
        ),
    ]