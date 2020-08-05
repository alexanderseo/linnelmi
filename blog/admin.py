from django.contrib import admin
from blog.models import Post, Categories


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date_pub', 'available',)
    list_filter = ('available', 'date_cre', 'date_pub')
    search_fields = ('title', 'post_body')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'date_pub'
    ordering = ('available', 'date_pub')


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'title',)

