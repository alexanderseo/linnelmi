from django.contrib import admin
from uslugi.models import Uslugi, Detailusluga, Document


class DocumentInline(admin.StackedInline):
    model = Document


@admin.register(Uslugi)
class UslugiAdmin(admin.ModelAdmin):
    list_display = ('name', 'title',)


@admin.register(Detailusluga)
class DetailuslugaAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'h1',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [DocumentInline]
