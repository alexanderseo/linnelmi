# Generated by Django 2.2.7 on 2019-12-04 23:30

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='SEO Title до 200 символов', max_length=200, verbose_name='Заголовок для SEO')),
                ('description', models.CharField(blank=True, help_text='Мета-описание для SEO до 450 символов', max_length=450, verbose_name='Мета-описание')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Название')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='URL-адрес')),
                ('post_body', ckeditor.fields.RichTextField(verbose_name='Текст статьи')),
                ('date_pub', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
                ('date_cre', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_upd', models.DateTimeField(auto_now=True, verbose_name='Последнее редактирование')),
                ('available', models.BooleanField(default=True, verbose_name='Активность')),
                ('img_post', models.ImageField(blank=True, upload_to='blogposts/%Y/', verbose_name='Загрузить изображения')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
