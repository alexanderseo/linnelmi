# Generated by Django 2.2.7 on 2019-11-17 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prepodovatel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='просто название элемента, оно не отображается', max_length=100, verbose_name='Название элемента')),
                ('minititle', models.CharField(blank=True, help_text='до 100 символов, небольшой текст над заголовком, необязательно', max_length=100, verbose_name='Минизаголовок')),
                ('title', models.CharField(help_text='Заголовок, до 200 символов, обязателен', max_length=200, verbose_name='Заголовок на странице')),
                ('textabout', models.TextField(blank=True, help_text='Описание под заголовком', verbose_name='Текстовое описание')),
                ('advantageone', models.CharField(blank=True, help_text='до 60 символов, необязательно', max_length=60, verbose_name='Преимущество 1')),
                ('advantageonetext', models.TextField(blank=True, help_text='описание преимущества, необязательно', verbose_name='Описание преимущества 1')),
                ('advantagetwo', models.CharField(blank=True, help_text='до 60 символов, необязательно', max_length=60, verbose_name='Преимущество 2')),
                ('advantagetwotext', models.TextField(blank=True, help_text='описание преимущества необязательно', verbose_name='Описание преимущества 2')),
                ('advantagethree', models.CharField(blank=True, help_text='до 60 символов, необязательно', max_length=60, verbose_name='Преимущество 3')),
                ('advantagethreetext', models.TextField(blank=True, help_text='описание преимущества необязательно', verbose_name='Описание преимущества 3')),
                ('prepodimg', models.ImageField(help_text='Изображение обрежется до 448x598px', upload_to='about/', verbose_name='Загрузить изображение')),
            ],
            options={
                'verbose_name': 'Блок обо мне',
                'verbose_name_plural': 'Блоки обо мне',
            },
        ),
    ]
