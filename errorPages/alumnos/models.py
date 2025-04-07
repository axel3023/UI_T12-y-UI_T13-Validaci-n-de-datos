from django.db import models
class Alumno(models.Model):
    #definir los atributos de clase
    nombre = models.CharField(max_length=55)
    apellido = models.CharField(max_length=55)
    edad = models.IntegerField()
    matricula = models.CharField(max_length=55, unique=True)
    correo = models.CharField(max_length=55,unique=True)

    def __str__(self):
        return self.nombre
