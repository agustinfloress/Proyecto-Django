from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Categoria(models.Model):
    
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre


class Post(models.Model):

    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='blog', null=True, blank=True)
    #el "upload_to='blog'" lo que hace es guardarme la imagen en una subcarpeta llamada "blog" de la carpeta "media"
    #sirve para tener un orden de las imagenes segun las apps que tengo creadas. 
    #el null y blank=True hace referencia a que la imagen es opcional, se puede agregar o no una imagen al post.
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    categorias=models.ManyToManyField(Categoria)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'

    def __str__(self):
        return self.titulo
