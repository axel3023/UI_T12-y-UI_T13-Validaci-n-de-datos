from django import forms
from .models import Categoria


#Podemos crear un formulario para cada modelo que exista
class categoriaForm(forms.ModelForm):
    #la clase meta(Metainfo del formulario)
    class Meta:
    #definir de que modelo se basa el formulario
        model = Categoria
    #Definir que campos seran incluidos en el formulario
        fields=['nombre','imagen']
    #Definir que atributos tienen los camps
        widgets ={
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre de la Categoria'
                }
            ),           
            'imagen': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Url de la imagen de la categoria'
                }
            )
        }

        labels ={
            'nombre':'Nombre de la Categoria',
            'imagen': 'URL de la imagen'
        }

        #Mensajes de error personalizados
        error_messages = {
            'nombre':{'required':'El nombre es obligatorio'},
            
        }