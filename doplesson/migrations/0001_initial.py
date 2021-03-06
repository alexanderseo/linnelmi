# Generated by Django 2.2.7 on 2019-12-21 17:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detailesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название элемента до 100 символов', max_length=100, verbose_name='Название')),
                ('title', models.CharField(help_text='Title для SEO до 200 символов', max_length=200, verbose_name='Заголовок для SEO')),
                ('description', models.CharField(blank=True, help_text='Мета-описание для SEO до 450 символов: необязательно', max_length=450, verbose_name='Мета-описание')),
                ('slug', models.SlugField(help_text='писать только латинскими буквами, вместо пробела тире', max_length=250, unique=True, verbose_name='URL-адрес')),
                ('h1', models.CharField(blank=True, help_text='Заголовок h1 на странице', max_length=100, verbose_name='Заголовок на странице')),
                ('minitext', models.CharField(blank=True, help_text='Описание под заголовком до 300 символов', max_length=300, verbose_name='Небольшое описание')),
                ('bigimg', models.ImageField(blank=True, help_text='Изображение размером 1920x1024', upload_to='uslugi/', verbose_name='Загрузить большое изображение')),
                ('podzagolovok', models.CharField(blank=True, help_text='Небольшой заголовок при необходимости', max_length=100, null=True, verbose_name='Подзаголовок')),
                ('bigtext', models.TextField(blank=True, help_text='Основной текст на странице', null=True, verbose_name='Основной текст')),
                ('uslugaimg', models.ImageField(blank=True, help_text='Изображение размером 473x630', upload_to='uslugi/', verbose_name='Загрузить небольшое изображение')),
                ('date_pub', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Английский - отдельная страница',
                'verbose_name_plural': 'Английский - отдельная страница',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Заголовок над документом до 150 символов', max_length=150, verbose_name='Заголовок документа')),
                ('docfile', models.FileField(blank=True, null=True, upload_to='files/', verbose_name='Загрузить файл')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата добавления')),
                ('materal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='doplesson.Detailesson')),
            ],
            options={
                'verbose_name': 'Документы',
            },
        ),
        migrations.CreateModel(
            name='Doplesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='заголовок для поисковой оптимизации до 200 символов', max_length=200, verbose_name='Заголовок страницы: title')),
                ('description', models.CharField(blank=True, help_text='мета-описание страницы для поисковой оптимизации до 450 символов, необязательно', max_length=450, verbose_name='Описание страницы: description')),
                ('name', models.CharField(help_text='заголовок для отображения на сайте до 200 символов', max_length=200, verbose_name='Название страницы')),
                ('minidescription', models.CharField(blank=True, help_text='текстовое описание под заголовком страницы, до 200 символов', max_length=200, verbose_name='Текстовое описание')),
                ('uslugiimg', models.ImageField(blank=True, help_text='размер 1920x1024 в идеале, но если что изображение обрежется', upload_to='contact/', verbose_name='Изображение на странице')),
            ],
            options={
                'verbose_name': 'Английский: общая информация на странице',
                'verbose_name_plural': 'Английский: общая информация на странице',
            },
        ),
        migrations.CreateModel(
            name='Dopfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='doplesson.Document')),
            ],
        ),
    ]
