# Generated by Django 2.2.7 on 2019-12-04 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uslugi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailusluga',
            name='bigtext',
            field=models.TextField(blank=True, help_text='Основной текст на странице', null=True, verbose_name='Основной текст'),
        ),
        migrations.AddField(
            model_name='detailusluga',
            name='podzagolovok',
            field=models.CharField(blank=True, help_text='Небольшой заголовок при необходимости', max_length=100, null=True, verbose_name='Подзаголовок'),
        ),
    ]
