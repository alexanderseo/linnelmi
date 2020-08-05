from django.db import models


class Slider(models.Model):
    name = models.CharField(max_length=100,
                            help_text='просто название слайда до 100 символов, оно не отображается',
                            verbose_name='Название слайда')
    title = models.CharField(blank=True,
                             max_length=150,
                             help_text='до 150 символов, заполнять необязательно',
                             verbose_name='Заголовок на слайде')
    description = models.CharField(blank=True,
                                   max_length=150,
                                   help_text='до 150 символов, заполнять необязательно',
                                   verbose_name='Тексто под заголовком')
    slideimg = models.ImageField(blank=False,
                                 upload_to='slider/',
                                 help_text='изображение обрежется до 1920x1024px, поэтому лучше брать большое',
                                 verbose_name='Добавить изображение')
    namebutton = models.CharField(blank=True,
                                  max_length=15,
                                  help_text='до 15 символов, необязательно',
                                  verbose_name='Название кнопки')
    linkbutton = models.URLField(blank=True,
                                 help_text='заполнить, если написали название кнопки',
                                 verbose_name='Ссылка на кнопку')

    class Meta:
        verbose_name = 'Блок 1.0: Слайдер'
        verbose_name_plural = 'Блок 1.0: Слайдеры'

    def __str__(self):
        return self.name


class Additionslider(models.Model):
    name = models.CharField(max_length=60,
                            help_text='Название элемента до 60 символов',
                            verbose_name='Имя элемента - новых не добавлять')
    geoname = models.CharField(max_length=60,
                               help_text='Имя месторасположения - например: Москва',
                               verbose_name='Имя места')
    koordinata_1 = models.CharField(max_length=50,
                                    help_text='формат написания: (55°45′07″)',
                                    verbose_name='Координата - 1')
    koordinata_2 = models.CharField(max_length=50,
                                    help_text='формат написания: (37°36′56″)',
                                    verbose_name='Координата - 2')
    link_to_map = models.URLField(verbose_name='Ссылка на карту Google или Yandex')
    anchor_1 = models.CharField(max_length=20,
                                blank=True,
                                help_text='имя анкора: Начало',
                                verbose_name='Анкор - Начало')
    anchor_2 = models.CharField(max_length=20,
                                blank=True,
                                help_text='имя анкора: Обо мне',
                                verbose_name='Анкор - Обо мне')
    anchor_3 = models.CharField(max_length=20,
                                blank=True,
                                help_text='имя анкора: Resume',
                                verbose_name='Анкор - Resume')
    anchor_4 = models.CharField(max_length=20,
                                blank=True,
                                help_text='имя анкора: Projects',
                                verbose_name='Анкор - Projects')
    anchor_5 = models.CharField(max_length=20,
                                blank=True,
                                help_text='имя анкора: Clients',
                                verbose_name='Анкор - Clients')

    class Meta:
        verbose_name = 'Блок 1.1: Слайдер - Дополнение'
        verbose_name_plural = 'Блок 1.1: Слайдер - Дополнения'

    def __str__(self):
        return self.name


class Prepodovatel(models.Model):
    name = models.CharField(max_length=100,
                            help_text='просто название элемента, оно не отображается',
                            verbose_name='Название элемента')
    minititle = models.CharField(max_length=100,
                                 blank=True,
                                 help_text='до 100 символов, небольшой текст над заголовком, необязательно',
                                 verbose_name='Минизаголовок')
    title = models.CharField(max_length=200,
                             help_text='Заголовок, до 200 символов, обязателен',
                             verbose_name='Заголовок на странице')
    textabout = models.TextField(blank=True,
                                 help_text='Описание под заголовком',
                                 verbose_name='Текстовое описание')
    advantageone = models.CharField(blank=True,
                                    max_length=60,
                                    help_text='до 60 символов, необязательно',
                                    verbose_name='Преимущество 1')
    advantageonetext = models.TextField(blank=True,
                                        help_text='описание преимущества, необязательно',
                                        verbose_name='Описание преимущества 1')
    advantagetwo = models.CharField(blank=True,
                                    max_length=60,
                                    help_text='до 60 символов, необязательно',
                                    verbose_name='Преимущество 2')
    advantagetwotext = models.TextField(blank=True,
                                        help_text='описание преимущества необязательно',
                                        verbose_name='Описание преимущества 2')
    advantagethree = models.CharField(blank=True,
                                      max_length=60,
                                      help_text='до 60 символов, необязательно',
                                      verbose_name='Преимущество 3')
    advantagethreetext = models.TextField(blank=True,
                                          help_text='описание преимущества необязательно',
                                          verbose_name='Описание преимущества 3')
    prepodimg = models.ImageField(blank=False,
                                  upload_to='about/',
                                  help_text='Изображение обрежется до 448x598px',
                                  verbose_name='Загрузить изображение')

    class Meta:
        verbose_name = 'Блок 2: Обо мне'
        verbose_name_plural = 'Блок 2: Обо мне'

    def __str__(self):
        return self.name


class Someaboutme(models.Model):
    name = models.CharField(max_length=100,
                            help_text='Навание элемента до 100 символов',
                            verbose_name='Имя элемента')
    zagolovok = models.CharField(max_length=100,
                                 blank=True,
                                 help_text='можно использовать html-теги: <span>, <br />',
                                 verbose_name='Заголовок')
    description = models.CharField(max_length=450,
                                   blank=True,
                                   help_text='Описание под заголовком до 450 символов',
                                   verbose_name='Текстовое описание')
    someimg = models.ImageField(blank=False,
                                upload_to='some/',
                                help_text='изображение обрежется до 1920x1024px, поэтому лучше брать большое',
                                verbose_name='Добавить изображение')
    titleleft = models.CharField(max_length=15,
                                 blank=True,
                                 help_text='Текст слева до 15 символов',
                                 verbose_name='Текст слева')

    class Meta:
        verbose_name = 'Блок 3.0: Под блоком обо мне'
        verbose_name_plural = 'Блок 3.0: Под блоком обо мне'

    def __str__(self):
        return self.name


class Counterelementy(models.Model):
    name = models.CharField(max_length=20,
                            help_text='имя элемента до 20 символов',
                            verbose_name='Название элемента')
    counter_1 = models.CharField(max_length=5,
                                 blank=True,
                                 null=True,
                                 help_text='Число до 5 символов',
                                 verbose_name='Счетчик - 1')
    counter_name_1 = models.CharField(max_length=20,
                                    blank=True,
                                    null=True,
                                    help_text='название до 20 символов',
                                    verbose_name='Названия для счетчика 1')
    counter_2 = models.CharField(max_length=5,
                                 blank=True,
                                 null=True,
                                 help_text='Число до 5 символов',
                                 verbose_name='Счетчик - 2')
    counter_name_2 = models.CharField(max_length=20,
                                      blank=True,
                                      null=True,
                                      help_text='название до 20 символов',
                                      verbose_name='Названия для счетчика 2')
    counter_3 = models.CharField(max_length=5,
                                 blank=True,
                                 null=True,
                                 help_text='Число до 5 символов',
                                 verbose_name='Счетчик - 3')
    counter_name_3 = models.CharField(max_length=20,
                                      blank=True,
                                      null=True,
                                      help_text='название до 20 символов',
                                      verbose_name='Названия для счетчика 3')
    counter_4 = models.CharField(max_length=5,
                                 blank=True,
                                 null=True,
                                 help_text='Число до 5 символов',
                                 verbose_name='Счетчик - 4')
    counter_name_4 = models.CharField(max_length=20,
                                      blank=True,
                                      null=True,
                                      help_text='название до 20 символов',
                                      verbose_name='Названия для счетчика 4')

    class Meta:
        verbose_name = 'Блок 3.1: Счетчик'
        verbose_name_plural = 'Блок 3.1: Счетчики'

    def __str__(self):
        return self.name


class Resume(models.Model):
    name = models.CharField(max_length=100,
                            help_text='Название элемента до 100 символов',
                            verbose_name='Имя элемента')
    minizagolovok = models.CharField(max_length=100,
                                     blank=True,
                                     help_text='небольшой заголовок до 100 символов',
                                     verbose_name='Заголовок H3')
    zagolovok = models.CharField(max_length=100,
                                 blank=True,
                                 help_text='Основной заголовок до 100 символов',
                                 verbose_name='Заголовок H2')
    description = models.CharField(max_length=450,
                                   blank=True,
                                   help_text='текстовое описание до 450 символов',
                                   verbose_name='Текстовое описание')

    class Meta:
        verbose_name = 'Блок 4: Блок резюме'
        verbose_name_plural = 'Блок 4: Блок резюме'

    def __str__(self):
        return self.name


class Resumeelement(models.Model):
    name = models.CharField(max_length=100,
                            help_text='название до 100 символов, обязательно к заполнению',
                            verbose_name='Название')
    title = models.CharField(max_length=100,
                             help_text='Заголовок в левом блоке',
                             verbose_name='Наименование этапа')
    period = models.CharField(max_length=40,
                              blank=True,
                              help_text='писать в формате: 2010-2013 года',
                              verbose_name='Период')
    titleright = models.CharField(max_length=100,
                                  blank=True,
                                  help_text='заголовок до 100 символов',
                                  verbose_name='Заголовок в правом блоке')
    description = models.TextField(blank=True,
                                   help_text='текстовое описание в блоке',
                                   verbose_name='Текстовый блок')
    nomer = models.CharField(max_length=10,
                             help_text='номер элемента в формате: 03.',
                             verbose_name='Номер элемента')

    class Meta:
        verbose_name = 'Блок 5: Элемент в резюме'
        verbose_name_plural = 'Блок 5: Элементы в резюме'

    def __str__(self):
        return self.name


class Myvideo(models.Model):
    name = models.CharField(max_length=100,
                            help_text='название элемента до 100 символов',
                            verbose_name='Название')
    video = models.CharField(max_length=150,
                             blank=True,
                             help_text='ссылка с YouTube',
                             verbose_name='Видео с YouTube')
    title = models.CharField(max_length=100,
                             blank=True,
                             help_text='заголовок до 100 символов',
                             verbose_name='Заголовок справа')
    description = models.TextField(blank=True,
                                   help_text='текстовое описание под заголовком',
                                   verbose_name='Описание')
    linkcanal = models.URLField(blank=True,
                                null=True,
                                help_text='Ссылка на канал с видео',
                                verbose_name='Ссылка на YouTube канал')
    namebutton = models.CharField(max_length=20,
                                  blank=True,
                                  help_text='название на кнопке до 20 символов',
                                  verbose_name='Название кнопки')

    class Meta:
        verbose_name = 'Блок 6: Видео презентация'
        verbose_name_plural = 'Блок 6: Видео презентация'

    def __str__(self):
        return self.name


class Urok(models.Model):
    name = models.CharField(max_length=100,
                            help_text='название элемента до 100 символов',
                            verbose_name='Название')
    title = models.CharField(max_length=100,
                             blank=True,
                             help_text='заголовок до 100 символов',
                             verbose_name='Заголовок')
    description = models.TextField(blank=True,
                                   help_text='описание под заголовком',
                                   verbose_name='Текстовое описание')

    class Meta:
        verbose_name = 'Блок 7.0: Для напоминаний'
        verbose_name_plural = 'Блок 7.0: Для напоминаний'

    def __str__(self):
        return self.name


class Itemurok(models.Model):
    name = models.CharField(max_length=100,
                            help_text='название элемента до 100 символов',
                            verbose_name='Имя элемента')
    title = models.CharField(max_length=60,
                             blank=True,
                             help_text='Заметка до 60 символов',
                             verbose_name='Заметка')
    podtitle = models.CharField(max_length=60,
                                blank=True,
                                help_text='дополнение до 60 символов',
                                verbose_name='Дополнение')
    itemimg = models.ImageField(blank=True,
                                null=True,
                                upload_to='urok/',
                                help_text='лучше вертикальное изображение',
                                verbose_name='Загрузить изображение')
    podurok = models.ForeignKey(Urok,
                                related_name='itemuroki',
                                null=True,
                                on_delete=models.CASCADE,
                                verbose_name='Напоминание')

    class Meta:
        verbose_name = 'Блок 7.1: элемент напоминания'
        verbose_name_plural = 'Блок 7.1: элементы напоминания'

    def __str__(self):
        return self.name


class Textblock(models.Model):
    name = models.CharField(max_length=50,
                            help_text='название элемента до 50 символов',
                            verbose_name='Название элемента')
    zagolovok = models.CharField(max_length=100,
                                 blank=True,
                                 null=True,
                                 help_text='заголовок до 100 символов',
                                 verbose_name='Заголовок')
    text_in_block = models.TextField(blank=True,
                                     null=True,
                                     help_text='текстовая область без ограничений',
                                     verbose_name='Текст')

    class Meta:
        verbose_name = 'Блок 8: Текстовый блок внизу'
        verbose_name_plural = 'Блок 8: Текстовый блок внизу'

    def __str__(self):
        return self.name


class Sociallink(models.Model):
    name = models.CharField(max_length=30,
                            help_text='название элемента до 30 символов',
                            verbose_name='Название элемента')
    linkvk = models.URLField(blank=True,
                             help_text='ссылка на соцсеть ВК',
                             verbose_name='Ссылка ВК')
    linkfb = models.URLField(blank=True,
                             help_text='ссылка на соцсеть FB',
                             verbose_name='Ссылка FB')
    linkinst = models.URLField(blank=True,
                               help_text='ссылка на соцсеть Instagram',
                               verbose_name='Ссылка Inst')
    linktw = models.URLField(blank=True,
                             help_text='ссылка на соцсеть Twitter',
                             verbose_name='Ссылка Twitter')

    class Meta:
        verbose_name = 'Ссылки на соцсети на всем сайте'
        verbose_name_plural = 'Ссылки на соцсети на всем сайте'

    def __str__(self):
        return self.name


class Footerblock(models.Model):
    name = models.CharField(max_length=50,
                            help_text='название элемента до 50 символов',
                            verbose_name='Название элемента')
    name_on_site = models.CharField(max_length=50,
                                    blank=True,
                                    null=True,
                                    help_text='Название выводится в футере, до 50 символов',
                                    verbose_name='Название в футере')
    telefone = models.CharField(max_length=20,
                                blank=True,
                                help_text='пишется ф формате: +7(999)-888-6655',
                                verbose_name='Номер телефона')
    email = models.EmailField(blank=True,
                              null=True,
                              help_text='пишется в формате email@email.ru',
                              verbose_name='Email')
    adress = models.CharField(max_length=60,
                              blank=True,
                              null=True,
                              help_text='адрес до 60 символов (город, район)',
                              verbose_name='Адрес')

    class Meta:
        verbose_name = 'Контактная информация в футере'
        verbose_name_plural = 'Контактная информация в футере'

    def __str__(self):
        return self.name


class Seohome(models.Model):
    name = models.CharField(max_length=50,
                            help_text='название элемента до 50 символов',
                            verbose_name='Название элемента')
    title = models.CharField(max_length=200,
                             blank=True,
                             null=True,
                             help_text='SEO заголовок на главную страницу до 200 символов',
                             verbose_name='Title для SEO')
    description = models.CharField(max_length=450,
                                   blank=True,
                                   null=True,
                                   help_text='Мета-описание для SEO до 450 символов',
                                   verbose_name='Description для главной страницы')

    class Meta:
        verbose_name = 'Блок 9: SEO для главной страницы'
        verbose_name_plural = 'Блок 9: SEO для главной страницы'

    def __str__(self):
        return self.name
