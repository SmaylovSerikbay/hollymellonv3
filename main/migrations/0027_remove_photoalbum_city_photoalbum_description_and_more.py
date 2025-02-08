# Generated by Django 5.0.6 on 2025-02-08 19:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_remove_photoalbum_venue_alter_photoalbum_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photoalbum',
            name='city',
        ),
        migrations.AddField(
            model_name='photoalbum',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='photoalbum',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.brand', verbose_name='Заведение'),
        ),
    ]
