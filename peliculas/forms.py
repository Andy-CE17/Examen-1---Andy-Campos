from django import forms
from .models import Director, Pelicula

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['nombre', 'nacionalidad']


class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'anio_estreno', 'genero', 'director']