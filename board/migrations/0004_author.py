# Generated by Django 4.2.7 on 2023-11-06 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_rename_relpy_reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('activation_code', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
