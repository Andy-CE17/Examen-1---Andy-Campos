from django.shortcuts import render, redirect
from .models import Director, Pelicula
from .forms import DirectorForm, PeliculaForm

def inicio(request):
    return render(request, 'peliculas/inicio.html')

def lista_directores(request):
    directores = Director.objects.all()
    return render(request, 'peliculas/lista_directores.html', {'directores': directores})

def lista_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'peliculas/lista_peliculas.html', {'peliculas': peliculas})

