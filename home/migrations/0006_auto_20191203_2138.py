# Generated by Django 2.2.7 on 2019-12-03 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20191201_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myvideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='название элемента до 100 символов', max_length=100, verbose_name='Название')),
                ('video', models.CharField(blank=True, help_text='ссылка с YouTube', max_length=150, verbose_name='Видео с YouTube')),
                ('title', models.CharField(blank=True, help_text='заголовок до 100 символов', max_length=100, verbose_name='Заголовок справа')),
                ('description', models.TextField(blank=True, help_text='текстовое описание под заголовком', verbose_name='Описание')),
                ('linkcanal', models.URLField(blank=True, help_text='Ссылка на канал с видео', null=True, verbose_name='Ссылка на YouTube канал')),
                ('namebutton', models.CharField(blank=True, help_text='название на кнопке до 20 символов', max_length=20, verbose_name='Название кнопки')),
            ],
            options={
                'verbose_name': 'Блок 6: Видео презентация',
                'verbose_name_plural': 'Блок 6: Видео презентация',
            },
        ),
        migrations.CreateModel(
            name='Urok',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='название элемента до 100 символов', max_length=100, verbose_name='Название')),
                ('title', models.CharField(blank=True, help_text='заголовок до 100 символов', max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, help_text='описание под заголовком', verbose_name='Текстовое описание')),
            ],
            options={
                'verbose_name': 'Блок 7: Для напоминаний',
                'verbose_name_plural': 'Блок 7: Для напоминаний',
            },
        ),
        migrations.AlterModelOptions(
            name='prepodovatel',
            options={'verbose_name': 'Блок 2: Обо мне', 'verbose_name_plural': 'Блок 2: Обо мне'},
        ),
        migrations.AlterModelOptions(
            name='resume',
            options={'verbose_name': 'Блок 4: Блок резюме', 'verbose_name_plural': 'Блок 4: Блок резюме'},
        ),
        migrations.AlterModelOptions(
            name='resumeelement',
            options={'verbose_name': 'Блок 5: Элемент в резюме', 'verbose_name_plural': 'Блок 5: Элементы в резюме'},
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name': 'Блок 1: Слайдер', 'verbose_name_plural': 'Блок 1: Слайдеры'},
        ),
        migrations.AlterModelOptions(
            name='someaboutme',
            options={'verbose_name': 'Блок 3: Под блоком обо мне', 'verbose_name_plural': 'Блок 3: Под блоком обо мне'},
        ),
        migrations.CreateModel(
            name='Itemurok',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='название элемента до 100 символов', max_length=100, verbose_name='Имя элемента')),
                ('title', models.CharField(blank=True, help_text='Заметка до 60 символов', max_length=60, verbose_name='Заметка')),
                ('podtitle', models.CharField(blank=True, help_text='дополнение до 60 символов', max_length=60, verbose_name='Дополнение')),
                ('podurok', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='itemuroki', to='home.Urok', verbose_name='Напоминание')),
            ],
            options={
                'verbose_name': 'Блок 7.1: элемент напоминания',
                'verbose_name_plural': 'Блок 7.1: элементы напоминания',
            },
        ),
    ]
