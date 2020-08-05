from django.urls import path
from . import views

app_name = 'materials'

urlpatterns = [
    path('', views.materials_list, name='materials_list'),
]
