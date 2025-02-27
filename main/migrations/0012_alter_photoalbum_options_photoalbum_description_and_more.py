# Generated by Django 5.1.6 on 2025-02-07 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_photoalbum_yandex_preview_url_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photoalbum',
            options={'ordering': ['-date', '-created_at'], 'verbose_name': 'Фотоальбом', 'verbose_name_plural': 'Фотоальбомы'},
        ),
        migrations.AddField(
            model_name='photoalbum',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='photoalbum',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликован'),
        ),
        migrations.AddField(
            model_name='photoalbum',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Порядок'),
        ),
        migrations.AddIndex(
            model_name='photoalbum',
            index=models.Index(fields=['city', '-date'], name='main_photoa_city_id_67639d_idx'),
        ),
        migrations.AddIndex(
            model_name='photoalbum',
            index=models.Index(fields=['is_published', '-date'], name='main_photoa_is_publ_ea9033_idx'),
        ),
    ]
