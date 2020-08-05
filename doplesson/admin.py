from django.contrib import admin
from doplesson.models import Doplesson, Detailesson, Document


class DocumentInline(admin.StackedInline):
    model = Document


@admin.register(Doplesson)
class DoplessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'title',)


@admin.register(Detailesson)
class DetailessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'h1',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [DocumentInline]
