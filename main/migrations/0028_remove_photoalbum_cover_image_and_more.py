# Generated by Django 5.0.6 on 2025-02-08 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_remove_photoalbum_city_photoalbum_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photoalbum',
            name='cover_image',
        ),
        migrations.RemoveField(
            model_name='photoalbum',
            name='description',
        ),
        migrations.RemoveField(
            model_name='photoalbum',
            name='title',
        ),
        migrations.AddField(
            model_name='photoalbum',
            name='photographer',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Фотограф'),
        ),
        migrations.AddField(
            model_name='photoalbum',
            name='photos',
            field=models.TextField(blank=True, help_text='Каждая ссылка на фото с новой строки', verbose_name='Список фотографий'),
        ),
    ]
