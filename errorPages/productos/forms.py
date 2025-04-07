from django import forms
from .models import Producto

#Podemos crear un formulario para cada modelo que exista
class productoForm(forms.ModelForm):
    #la clase meta(Metainfo del formulario)
    class Meta:
    #definir de que modelo se basa el formulario
        model = Producto
    #Definir que campos seran incluidos en el formulario
        fields=['nombre','precio','imagen','categoria']
    #Definir que atributos tienen los camps
        widgets ={
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del Producto'
                }
            ),
            'precio':forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Precio'
                }
            ),
            'imagen': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Url de la imagen del producto'
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ) 
        }

        labels ={
            'nombre':'Nombre del producto',
            'precio': 'Precio (MXN)',
            'imagen': 'URL de la imagen',
            'categoria':'Categoria del producto'
        }

        #Mensajes de error personalizados
        error_messages = {
            'nombre':{'required':'El nombre es obligatorio'},
            'precio':{'required': 'El precio no puede estar vacio', 'invalid':'Ingrese un numero valido'}
        }