# Generated by Django 2.2.7 on 2019-11-17 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='просто название слайда до 100 символов, оно не отображается', max_length=100, verbose_name='Название слайда')),
                ('title', models.CharField(blank=True, help_text='до 150 символов, заполнять необязательно', max_length=150, verbose_name='Заголовок на слайде')),
                ('description', models.CharField(blank=True, help_text='до 150 символов, заполнять необязательно', max_length=150, verbose_name='Тексто под заголовком')),
                ('slideimg', models.ImageField(help_text='изображение обрежется до 1920x1024px, поэтому лучше брать большое', upload_to='slider/', verbose_name='Добавить изображение')),
                ('namebutton', models.CharField(blank=True, help_text='до 15 символов, необязательно', max_length=15, verbose_name='Название кнопки')),
                ('linkbutton', models.URLField(blank=True, help_text='заполнить, если написали название кнопки', verbose_name='Ссылка на кнопку')),
            ],
            options={
                'verbose_name': 'Слайдер',
                'verbose_name_plural': 'Слайдеры',
            },
        ),
    ]
