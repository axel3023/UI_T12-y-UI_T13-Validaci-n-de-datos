from django.urls import path
from .views import *

urlpatterns = [
    path('verCategoria/',ver_categorias,name='verCategoria'),
    path('agregarCategoria/',agregar_categoria, name='agregarCategoria'),
    path('api/get/',lista_categoria,name='lista'),
    path('json/',json_view,name='json'),
    path('api/post/',registrar_categoria,name='post')
]