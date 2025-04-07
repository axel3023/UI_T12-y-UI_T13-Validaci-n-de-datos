from django.db import models

class ErrorLog(models.Model):
    #Lo mismo que poner varChar(10)
    codigo = models.CharField(max_length=10)
    #Lo mismo que poner un lontText
    mensaje = models.TextField()
    #Lo mismo que Date(now())
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{codigo} - {mensaje}"