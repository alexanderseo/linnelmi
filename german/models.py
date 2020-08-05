from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class German(models.Model):
    title = models.CharField(max_length=200,
                             help_text='заголовок для поисковой оптимизации до 200 символов',
                             verbose_name='Заголовок страницы: title')
    description = models.CharField(max_length=450,
                                   blank=True,
                                   help_text='мета-описание страницы для поисковой оптимизации до 450 символов, необязательно',
                                   verbose_name='Описание страницы: description')
    name = models.CharField(max_length=200,
                            help_text='заголовок для отображения на сайте до 200 символов',
                            verbose_name='Название страницы')
    minidescription = models.CharField(max_length=200,
                                       blank=True,
                                       help_text='текстовое описание под заголовком страницы, до 200 символов',
                                       verbose_name='Текстовое описание')
    uslugiimg = models.ImageField(blank=True,
                                  upload_to='contact/',
                                   help_text='размер 1920x1024 в идеале, но если что изображение обрежется',
                                   verbose_name='Изображение на странице')

    class Meta:
        verbose_name = 'Немецкий: общая информация на странице'
        verbose_name_plural = 'Немецкий: общая информация на странице'

    def __str__(self):
        return self.name


class Detailgerman(models.Model):
    name = models.CharField(max_length=100,
                            help_text='Название элемента до 100 символов',
                            verbose_name='Название')
    title = models.CharField(max_length=200,
                             help_text='Title для SEO до 200 символов',
                             verbose_name='Заголовок для SEO')
    description = models.CharField(max_length=450,
                                   blank=True,
                                   help_text='Мета-описание для SEO до 450 символов: необязательно',
                                   verbose_name='Мета-описание')
    slug = models.SlugField(max_length=250,
                            unique=True,
                            help_text='писать только латинскими буквами, вместо пробела тире',
                            verbose_name='URL-адрес')
    h1 = models.CharField(max_length=100,
                          blank=True,
                          help_text='Заголовок h1 на странице',
                          verbose_name='Заголовок на странице')
    minitext = models.CharField(max_length=300,
                                blank=True,
                                help_text='Описание под заголовком до 300 символов',
                                verbose_name='Небольшое описание')
    bigimg = models.ImageField(blank=True,
                               upload_to='uslugi/',
                               help_text='Изображение размером 1920x1024',
                               verbose_name='Загрузить большое изображение')
    podzagolovok = models.CharField(max_length=100,
                                    blank=True,
                                    null=True,
                                    help_text='Небольшой заголовок при необходимости',
                                    verbose_name='Подзаголовок')
    bigtext = models.TextField(blank=True,
                               null=True,
                               help_text='Основной текст на странице',
                               verbose_name='Основной текст')
    uslugaimg = models.ImageField(blank=True,
                                  upload_to='uslugi/',
                                  help_text='Изображение размером 473x630',
                                  verbose_name='Загрузить небольшое изображение')
    date_pub = models.DateTimeField(default=timezone.now,
                                    verbose_name='Дата публикации')

    class Meta:
        verbose_name = 'Немецкий - отдельная страница'
        verbose_name_plural = 'Немецкий - отдельная страница'

    def __str__(self):
        return self.name


class Document(models.Model):
    materal = models.ForeignKey(Detailgerman,
                                related_name='documents',
                                on_delete=models.CASCADE)
    title = models.CharField(max_length=150,
                             blank=True,
                             help_text='Заголовок над документом до 150 символов',
                             verbose_name='Заголовок документа')
    docfile = models.FileField(upload_to='files/',
                               blank=True,
                               null=True,
                               verbose_name='Загрузить файл')
    publish = models.DateTimeField(default=timezone.now,
                                   verbose_name='Дата добавления')

    class Meta:
        verbose_name = 'Документы'

    def __str__(self):
        return self.title


class Filegerman(models.Model):
    module = models.ForeignKey(Document,
                               related_name='contents',
                               on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
