from django.urls import path
from YokoCino.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name= 'Home'),
    path('inicio/', inicio, name='Inicio'),
    path('setPost/', setPost, name="setPost"),
    path('setCategoria/', setCategoria, name="setCategoria"),
    path('setAutor/', setAutor, name="setAutor"),
    path('ensaladas/', ensaladas, name = 'Ensaladas'),
    path('carnes/', carnes, name = 'Carnes'),
    path('guisos/', guisos, name = 'Guisos'),
    path('about/', about, name='About'),
    path('post/editar/<slug:slug>/', editPost, name='editar_post'),
    path('post/<slug:slug>/',detallePost, name = 'detalle_post'),
]
"""
detalle_post y editar_post usan <slug:slug> para poder identificarlos sin utilizar un id interno
"""

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)