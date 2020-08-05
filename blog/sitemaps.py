from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Categories, Post


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.objects.filter(available=True)

    def lastmod(self, obj):
        return obj.date_upd


class CategoriesSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return Categories.objects.all()


class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = 'daily'

    def items(self):
        return ['home:index',
                'uslugi:uslugi',
                'german:germani',
                'materials:materials_list',
                'contact:contact',
                'blog:post_list', ]

    def location(self, item):
        return reverse(item)
