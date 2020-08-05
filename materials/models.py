from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Materials(models.Model):
    title = models.CharField(max_length=200,
                             help_text='заголовок для SEO до 200 символов',
                             verbose_name='Title для SEO')
    description = models.CharField(max_length=450,
                                   blank=True,
                                   help_text='Мета-описание для SEO, до 450 символов, необязательно')
    h1 = models.CharField(max_length=150,
                          help_text='Заголовок на странице, обязателен',
                          verbose_name='Заголовок на странице')
    matimg = models.ImageField(upload_to='materials/',
                               help_text='изображение лучше брать вертикальное, обрежется до 960x1300',
                               verbose_name='Загрузить изображение для оформдения страницы')

    class Meta:
        verbose_name = 'Страница материалов'
        verbose_name_plural = 'Страницы материалов'

    def __str__(self):
        return self.h1


class Document(models.Model):
    materal = models.ForeignKey(Materials,
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


class Content(models.Model):
    module = models.ForeignKey(Document,
                               related_name='contents',
                               on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
