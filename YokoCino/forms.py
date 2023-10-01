from django import forms
from YokoCino.models import *

class formSetPost(forms.ModelForm):
    imagen = forms.ImageField(required=False)
    class Meta:
        model = Post
        fields = ['titulo', 'slug', 'descripcion', 'contenido', 'imagen', 'autor', 'categoria', 'estado']

"""
Form utilizado para crear un nuevo Post
* la primer linea hace que no sea necesario adjuntar una imagen
"""

class formSetCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'estado']

"""
Form utilizado para crear una nueva Categoria, porque el listado no es taxativo
"""

class formSetAutor(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellido', 'link', 'email', 'estado']

"""
Form utilizado para crear una nuevo Autor
"""