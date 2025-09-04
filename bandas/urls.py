from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_bandas, name='lista_bandas'),
    path('<str:banda_id>/', views.lista_albumes, name='lista_albumes'),
    path('<str:banda_id>/<str:album_id>/', views.lista_canciones, name='lista_canciones'),
]
