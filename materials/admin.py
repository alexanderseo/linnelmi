from django.contrib import admin
from materials.models import Materials, Document


class DocumentInline(admin.StackedInline):
    model = Document


@admin.register(Materials)
class MaterialsAdmin(admin.ModelAdmin):
    list_display = ['title', 'h1', ]
    inlines = [DocumentInline]



# @admin.register(Document)
# class DocumentAdmin(admin.ModelAdmin):
    # list_display = ['title',]
