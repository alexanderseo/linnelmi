from django.urls import path
from . import views

app_name = 'doplesson'

urlpatterns = [
    path('<slug:slug_doplesson>', views.doplesson_single, name='doplesson_single'),
    path('', views.doplesson_list, name='doplesson_list'),
]
