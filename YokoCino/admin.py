from django.contrib import admin
from .models import *
from Accounts.models import *

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre','estado','fecha_creacion',)

class AutorAdmin(admin.ModelAdmin):
    search_fields = ['nombre','apellido','email']
    list_display = ('nombre','apellido','email','estado','fecha_creacion',)

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Post)
admin.site.register(Avatar)