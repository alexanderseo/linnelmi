# Generated by Django 2.2.7 on 2019-12-15 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_additionslider_counterelementy_sociallink_textblock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footerblock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='название элемента до 50 символов', max_length=50, verbose_name='Название элемента')),
                ('name_on_site', models.CharField(blank=True, help_text='Название выводится в футере, до 50 символов', max_length=50, null=True, verbose_name='Название в футере')),
                ('telefone', models.CharField(blank=True, help_text='пишется ф формате: +7(999)-888-6655', max_length=20, verbose_name='Номер телефона')),
                ('email', models.EmailField(blank=True, help_text='пишется в формате email@email.ru', max_length=254, null=True, verbose_name='Email')),
                ('adress', models.CharField(blank=True, help_text='адрес до 60 символов (город, район)', max_length=60, null=True, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Контактная информация в футере',
                'verbose_name_plural': 'Контактная информация в футере',
            },
        ),
        migrations.AlterModelOptions(
            name='additionslider',
            options={'verbose_name': 'Блок 1.1: Слайдер - Дополнение', 'verbose_name_plural': 'Блок 1.1: Слайдер - Дополнения'},
        ),
        migrations.AlterModelOptions(
            name='counterelementy',
            options={'verbose_name': 'Блок 3.1: Счетчик', 'verbose_name_plural': 'Блок 3.1: Счетчики'},
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name': 'Блок 1.0: Слайдер', 'verbose_name_plural': 'Блок 1.0: Слайдеры'},
        ),
        migrations.AlterModelOptions(
            name='someaboutme',
            options={'verbose_name': 'Блок 3.0: Под блоком обо мне', 'verbose_name_plural': 'Блок 3.0: Под блоком обо мне'},
        ),
    ]
