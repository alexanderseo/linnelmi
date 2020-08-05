from django.db import models


class Contact(models.Model):
    title = models.CharField(max_length=200,
                             help_text='заголовок для поисковой оптимизации до 200 символов',
                             verbose_name='Заголовок страницы: title')
    description = models.CharField(max_length=450,
                                   blank=True,
                                   help_text='мета-описание страницы для поисковой оптимизации до 450 символов, необязательно', verbose_name='Описание страницы: description')
    name = models.CharField(max_length=200,
                            help_text='заголовок для отображения на сайте до 200 символов',
                            verbose_name='Название страницы')
    minidescription = models.CharField(max_length=200,
                                       blank=True,
                                       help_text='текстовое описание под заголовком страницы, до 200 символов', verbose_name='Текстовое описание')
    contactimg = models.ImageField(blank=True,
                                   upload_to='contact/',
                                   help_text='размер 1920x1024 в идеале, но если что изображение обрежется', verbose_name='Изображение на странице')
    contacttitle = models.CharField(max_length=100,
                                    blank=True,
                                    help_text='до 100 символов',
                                    verbose_name='Мини заголовок')
    contactdescription = models.CharField(max_length=100,
                                          blank=True,
                                          help_text='до 100 символов',
                                          verbose_name='Мини описание')
    phonename = models.CharField(max_length=60,
                                 help_text='название до 60 символов',
                                 verbose_name='Название поля: телефон')
    phone = models.CharField(max_length=25,
                             blank=True,
                             help_text='до 25 символов, необязательно',
                             verbose_name='Номер телефона')
    adressname = models.CharField(max_length=60,
                                  help_text='название до 60 символов',
                                  verbose_name='Название поля: адрес')
    adress = models.CharField(max_length=100,
                              blank=True,
                              help_text='до 100 символов, необязательно',
                              verbose_name='Адрес')
    nameemail = models.CharField(max_length=60,
                                 help_text='название до 60 символов',
                                 verbose_name='Название поля: email')
    email = models.EmailField(blank=True,
                              help_text='формат eeee@eee.ru, необязательно',
                              verbose_name='Email')

    class Meta:
        verbose_name = 'Информация на странице контактов'
        verbose_name_plural = 'Информация на странице контактов'

    def __str__(self):
        return self.name
