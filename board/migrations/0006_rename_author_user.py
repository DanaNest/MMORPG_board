# Generated by Django 4.2.7 on 2023-11-06 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_alter_post_content'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='User',
        ),
    ]