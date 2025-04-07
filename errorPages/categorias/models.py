from django.db import models

class Categoria(models.Model):
    #definir los atributos de clase
    nombre = models.CharField(max_length=100)
    imagen = models.URLField()

    def __str__(self):
        return self.nombre
