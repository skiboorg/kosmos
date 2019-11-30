# Generated by Django 2.2.7 on 2019-11-30 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20191119_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='seotag',
            name='fbPixel',
            field=models.TextField(blank=True, null=True, verbose_name='Код пикселя'),
        ),
        migrations.AddField(
            model_name='seotag',
            name='googleTAG',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Код подтверждения google'),
        ),
        migrations.AddField(
            model_name='seotag',
            name='yandexMetrika',
            field=models.TextField(blank=True, null=True, verbose_name='Код Яндекс метрики'),
        ),
        migrations.AddField(
            model_name='seotag',
            name='yandexTAG',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Код подтверждения Яндекс'),
        ),
    ]
