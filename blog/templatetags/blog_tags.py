from django import template
from blog.models import Post, Categories

register = template.Library()


@register.inclusion_tag('layouts/widget_blog_posts.html')
def widget_blog_posts():
    posts_mini = Post.objects.all()[:4]
    return {'posts_mini': posts_mini, }


@register.inclusion_tag('layouts/widget_blog_category.html')
def widget_blog_category():
    cat_mini = Categories.objects.all()[:4]
    return {'cat_mini': cat_mini, }
