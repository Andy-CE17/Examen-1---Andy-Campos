from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('directores/', views.lista_directores, name='lista_directores'),
    path('peliculas/', views.lista_peliculas, name='lista_peliculas'),
]