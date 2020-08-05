from django.contrib import admin
from home.models import *


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'title',)


@admin.register(Additionslider)
class AdditionsliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'geoname',)


@admin.register(Prepodovatel)
class PrepodovatelAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'minititle',)


@admin.register(Someaboutme)
class SomeaboutmeAdmin(admin.ModelAdmin):
    list_display = ('name', 'zagolovok', 'description',)


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'zagolovok',)


@admin.register(Resumeelement)
class ResumeelementAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'period',)


@admin.register(Urok)
class UrokAdmin(admin.ModelAdmin):
    list_display = ('name', 'title',)


@admin.register(Itemurok)
class ItemurokAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')


@admin.register(Myvideo)
class MyvideAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')


@admin.register(Textblock)
class TextblockAdmin(admin.ModelAdmin):
    list_display = ('name', 'zagolovok',)


@admin.register(Sociallink)
class SociallinkAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Counterelementy)
class CounterelementyAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Footerblock)
class FooterblockAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_on_site',)


@admin.register(Seohome)
class SeohomeAdmin(admin.ModelAdmin):
    list_display = ('name', 'title',)


admin.site.site_title = 'Личный кабинет сайта'
admin.site.site_header = 'Личный кабинет'
