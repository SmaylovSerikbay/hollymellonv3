# Generated by Django 5.0.6 on 2025-02-08 18:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_venue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photoalbum',
            name='cover_image',
        ),
        migrations.RemoveField(
            model_name='photoalbum',
            name='yandex_preview_url',
        ),
        migrations.AddField(
            model_name='photoalbum',
            name='cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to='album_covers/', verbose_name='Обложка альбома'),
        ),
        migrations.AddField(
            model_name='photoalbum',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активен'),
        ),
        migrations.AddField(
            model_name='photoalbum',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
        migrations.AddField(
            model_name='photoalbum',
            name='venue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.venue', verbose_name='Заведение'),
        ),
        migrations.AlterField(
            model_name='photoalbum',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='photoalbum',
            name='date',
            field=models.DateField(verbose_name='Дата мероприятия'),
        ),
        migrations.AlterField(
            model_name='photoalbum',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название альбома'),
        ),
        migrations.AlterField(
            model_name='photoalbum',
            name='yandex_folder',
            field=models.CharField(max_length=500, verbose_name='Путь к папке на Яндекс.Диске'),
        ),
    ]
