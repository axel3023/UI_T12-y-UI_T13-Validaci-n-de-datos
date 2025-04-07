from django.shortcuts import render,redirect
from .models import Categoria
from .forms import categoriaForm
from django.http import JsonResponse
import json

#Agregar producto
def agregar_categoria(request):
    #Primero checamos como llegamos a esta funcion
    if request.method == 'POST':
        #Llegamos aqui por el envio de un formulario
        form = categoriaForm(request.POST)#Genera un formulario lleno con informacion"La que envio el usuario"
        if form.is_valid():
            form.save()
            return redirect('ver')#Redirige a la lista de productos
    else:
        form = categoriaForm()
    return render(request,'agregarCategoria.html',{'form':form})

#Ver los productos
def ver_categorias(request):
    categorias = Categoria.objects.all()
    return render(request,'verCategoria.html',{'categorias':categorias})

#Devuelve el json
def lista_categoria(request):
    categorias = Categoria.objects.all()
    #Para enviar un json debemos escribir los datos en un diccionario usando {}
    #Diccionario personalizado
    data=[
        {
            'nombre': p.nombre,
            'imagen': p.imagen
        }
        for p in categorias
    ]
    return JsonResponse(data,safe=False)

def json_view(request):
    return render(request,'json.html')

def registrar_categoria(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nueva_categoria = Categoria.objects.create(
                nombre=data['nombre'],
                imagen=data['imagen']
            )
            return JsonResponse({
                'mensaje': 'Registro exitoso',
                'id': nueva_categoria.id
            },status =201
            )
        except Exception as e:
            return JsonResponse({
                'error': str(e)
            },status=400)
    return JsonResponse({
        'error':'Método no es POST'

    },status=405)
