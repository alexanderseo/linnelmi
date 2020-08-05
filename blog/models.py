from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.urls import reverse


class Categories(models.Model):
    name = models.CharField(max_length=50,
                            help_text='просто название категории до 50 символов',
                            verbose_name='Название элемента - категории')
    title = models.CharField(max_length=200,
                             db_index=True,
                             help_text='SEO заголовок до 200 символов',
                             verbose_name='Заголовок категории - Title')
    description = models.CharField(max_length=450,
                                   blank=True,
                                   help_text='Мета-описание для SEO до 450 символов',
                                   verbose_name='Description категории')
    slug = models.SlugField(max_length=250,
                            unique=True,
                            help_text='использовать латинские символы и тире',
                            verbose_name='URL-адрес')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:post_list_by_categories', args=[self.slug])


class Post(models.Model):
    title = models.CharField(max_length=200,
                             help_text='SEO Title до 200 символов',
                             verbose_name='Заголовок для SEO')
    description = models.CharField(max_length=450,
                                   blank=True,
                                   help_text='Мета-описание для SEO до 450 символов',
                                   verbose_name='Мета-описание')
    name = models.CharField(max_length=200,
                            db_index=True,
                            verbose_name='Название')
    slug = models.SlugField(max_length=250,
                            unique=True,
                            verbose_name='URL-адрес')
    post_body = RichTextField(verbose_name='Текст статьи')
    date_pub = models.DateTimeField(default=timezone.now,
                                    verbose_name='Дата публикации')
    date_cre = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата создания')
    date_upd = models.DateTimeField(auto_now=True,
                                    verbose_name='Последнее редактирование')
    available = models.BooleanField(default=True,
                                    verbose_name='Активность')
    img_post = models.ImageField(blank=True,
                                 upload_to='blogposts/%Y/',
                                 verbose_name='Загрузить изображения')
    categories = models.ForeignKey(Categories,
                                   related_name='posts',
                                   null=True,
                                   on_delete=models.PROTECT,
                                   verbose_name='Категория')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.categories.slug, self.slug])


class Widgetaboutme(models.Model):
    name = models.CharField(max_length=50,
                            help_text='название элемента виджета до 50 символов',
                            verbose_name='Название виджета')
    title_widget = models.CharField(max_length=20,
                                    help_text='Заголовок для отображения на сайте',
                                    verbose_name='Заголовок виджета')
    pass
