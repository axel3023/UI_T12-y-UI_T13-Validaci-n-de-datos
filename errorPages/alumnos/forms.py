from django import forms
from .models import Alumno

class alumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre','apellido','edad','matricula','correo']
        widgets={
            'nombre':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Nombre del Alumno'
                }
            ),
            'apellido':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Apellido del Alumno'
                }
            ),
            'edad':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeolder':'Edad del alumno'
                }
            ),
            'matricula':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Matricula del alumno'
                }
            ),
            'correo':forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Correo del alumno'
                }

            )
        }

        labels={
            'nombre':'Nombre del alumno',
            'apellido':'Apellido del alumno',
            'edad':'Edad del alumno',
            'matricula':'Matricula del alumno',
            'correo':'Correo del alumno'
        }

        error_messages={
            'nombre':{'required':'El nombre es obligatorio'},
            'apellido':{'required':'El apellido es obligatorio'},
            'edad':{'required':'La edad es obligatoria'},
            'matricula':{'required':'La matricula es obligatoria'},
            'correo':{'required':'El correo es obligatorio'}
        }