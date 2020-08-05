from django.urls import path
from . import views

app_name = 'uslugi'

urlpatterns = [
    path('<slug:slug_usluga>', views.usluga, name='usluga'),
    path('', views.uslugi, name='uslugi'),
]
