from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import AlumnoViewSet
from .views import agregar_alumno

router = SimpleRouter()
router.register(r'api',AlumnoViewSet)

urlpatterns=[
    path ('',include(router.urls)),
    path('agregarAlumno/',agregar_alumno,name='agregar_alumnos')
]