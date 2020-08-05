from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from blog.models import Post, Categories


def post_list(request, category_slug=None):
    category = None
    categories = Categories.objects.all()
    posts = Post.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Categories, slug=category_slug)
        posts = posts.filter(categories=category)
    paginator = Paginator(posts, 4)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    return render(request, 'blog/blog_list.html', {'category': category,
                                                   'categories': categories,
                                                   'posts': page.object_list,
                                                   'page': page, })


def post_detail(request, category_slug=None, post_slug=None):
    category = None
    categories = Categories.objects.all()
    posts = Post.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Categories, slug=category_slug)
        post = get_object_or_404(Post, categories=category, slug=post_slug, available=True)
    return render(request, 'blog/blog_detail.html', {'post': post,
                                                     'posts': posts,
                                                     'categories': categories, })
