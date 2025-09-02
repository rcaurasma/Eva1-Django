from django.urls import path
from . import views

urlpatterns = [
    path('', views.bandas, name='bandas'),
    path('banda/<str:banda_id>/', views.albumes, name='albumes'),
    path('banda/<str:banda_id>/album/<str:album_id>/', views.canciones, name='canciones'),
]
