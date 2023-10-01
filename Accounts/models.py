from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    
    def __str__(self):
        return f"{self.user} - {self.imagen}"
    
"""
Avatar es requisito para la entrega. Se conecta con el usuario mediante una llave foranea y se sube a 'media/avatares/
> se le permite tambien poseer un valor blanco o nulo, para hacerlo no obligatorio
"""
    
class UserLink(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = models.CharField('Descripcion',max_length=100,null=True, blank=True)
    link = models.URLField('Link',null=True, blank=True)

"""
UserLink es un modelo accesorio de user, para completar los datos que pide la entrega
> agrega unicamente esos dos campos, y se relaciona uno a uno con el modelo User por defecto
> es tambien requisito de la entrega
"""

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

"""
Message es el modelo de la mensajeria interna del proyecto
* posee un remitente y un destinatario ligados por llaves foráneas al usuario que tambien se eliminan en cascada si este se eliminase
> traen tambien un timestamp para reconocer horario
> content es el cuerpo del mensaje
"""