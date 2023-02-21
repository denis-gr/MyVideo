# Generated by Django 4.1.7 on 2023-02-17 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videopage',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='videopage',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='videopage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Превью'),
        ),
        migrations.AlterField(
            model_name='videopage',
            name='original_size_height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='videopage',
            name='original_size_width',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='videopage',
            name='original_video',
            field=models.FileField(upload_to='', verbose_name='Оригинал видео'),
        ),
    ]
