# Generated by Django 4.2.7 on 2023-11-06 22:44

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0012_post_content2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Текст'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='content2',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]