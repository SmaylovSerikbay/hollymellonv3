# Generated by Django 5.0.6 on 2025-02-08 19:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_remove_photoalbum_cover_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя фотографа')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('order', models.IntegerField(default=0, verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Фотограф',
                'verbose_name_plural': 'Фотографы',
                'ordering': ['order', 'name'],
            },
        ),
        migrations.RemoveField(
            model_name='photoalbum',
            name='photos',
        ),
        migrations.AlterField(
            model_name='photoalbum',
            name='photographer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.photographer', verbose_name='Фотограф'),
        ),
    ]
