from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('<slug:category_slug>/<slug:post_slug>/', views.post_detail, name='post_detail'),
    path('<slug:category_slug>/', views.post_list, name='post_list_by_categories'),
    path('', views.post_list, name='post_list'),
]
