# Generated by Django 4.2.7 on 2023-11-09 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='code',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='verification_code',
            field=models.CharField(default='', max_length=6),
            preserve_default=False,
        ),
    ]
