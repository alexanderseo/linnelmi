from django.urls import path
from . import views

app_name = 'german'

urlpatterns = [
    path('<slug:slug_usluga>', views.german, name='german'),
    path('', views.germani, name='germani'),
]
