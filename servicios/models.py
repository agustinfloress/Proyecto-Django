from django.db import models

# Create your models here.

class Servicio(models.Model):

    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='servicios')
    #el "upload_to='servicios'" lo que hace es guardarme la imagen en una subcarpeta llamada "servicios" de la carpeta "media"
    #sirve para tener un orden de las imagenes segun las apps que tengo creadas. 
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'

    def __str__(self):
        return self.titulo
