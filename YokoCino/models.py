from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
    
class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de categoría',max_length = 50, null= False, blank= False)
    estado = models.BooleanField('Categoría activada/Categoría desactivada', default=True)
    fecha_creacion = models.DateField('Fecha de Creación',auto_now= False, auto_now_add= True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
    
    def __str__(self):
        return self.nombre

"""
El modelo Categoria sirve para categorizar posts. Las mismas pueden activarse o desactivarse para permanecer ocultas
"""

class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de Autor',max_length = 50, null= False, blank= False)
    apellido = models.CharField('Apellido de Autor',max_length = 50, null= False, blank= False)
    link = models.URLField('Link', null = True, blank = True)
    email = models.EmailField ('Email', null = False, blank = False)
    estado = models.BooleanField('Autor activado/Autor desactivado', default=True)
    fecha_creacion = models.DateField('Fecha de Creación',auto_now= False, auto_now_add= True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    def __str__(self):
        return '{0},{1}'.format(self.apellido, self.nombre)

"""
El modelo Autor funciona de manera similar, con mas informacion de usuario personalizable
"""

class Post(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo',max_length = 100, null= False, blank= False)
    slug = models.CharField('Slug',max_length = 100, null= False, blank= False)
    descripcion = models.CharField('Descripcion',max_length = 150, null= False, blank= False)
    contenido = RichTextField('Contenido')
    imagen = models.ImageField(upload_to='blogimg', null=True, blank=True)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado/No publicado', default = True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now = False, auto_now_add= True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo
    
"""
Post es el modelo principal del blog.
* slug sirve para pasarse luego por url y mostrar en produccion la informacion completa
* se agrego ckeditor para poder editar de manera mas comoda desde el admin y se muestre mejor en produccion
* en caso de eliminarse autor o categoria, se eliminarian tambien en cascada de la base de datos
"""