# Generated by Django 4.2.7 on 2023-11-12 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0018_response_delete_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='status',
            field=models.CharField(choices=[('undefined', 'Неопределенный'), ('accepted', 'Принят'), ('rejected', 'Отклонен')], default='undefined', max_length=10),
        ),
    ]
