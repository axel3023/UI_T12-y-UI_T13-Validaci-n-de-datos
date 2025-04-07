from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ProductoViewSet
from .views import agregar_producto
from.views import prueba_view


router = SimpleRouter()
router.register(r'api',ProductoViewSet)

urlpatterns=[
    path ('',include(router.urls)),
    path('agregar/',agregar_producto,name='agregar_productos'),
    path('prueba/',prueba_view,name='prueba')
]