from django.contrib import admin
from german.models import German, Detailgerman, Document


class DocumentInline(admin.StackedInline):
    model = Document


@admin.register(German)
class GermanAdmin(admin.ModelAdmin):
    list_display = ('name', 'title',)


@admin.register(Detailgerman)
class DetailgermanAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'h1',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [DocumentInline]
