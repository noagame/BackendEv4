from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'cliente',ClienteViewSet) # Ruta /api/clientes/
router.register(r'trabajadore',TrabajadorViewSet) # Ruta /api/trabajador/
router.register(r'horario',HorarioViewSet) # Ruta /api/horario/
router.register(r'cita',CitasViewSet) # Ruta /api/citas/

urlpatterns = [
    path('api/', include(router.urls)), #Incluye las rutas generadas por el router
    # Ruta Home
    path('', home, name='home'),
    # Rutas de login - logout
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', signout, name='logout'),
    # Vistas CRUD Templates Clientes
    path('clientes/', cliente_list, name='cliente_list'),
    path('clientes/create', cliente_create, name='cliente_create'),
    path('clientes/update/<int:pk>', cliente_update, name='cliente_update'),
    path('clientes/delete/<int:pk>', cliente_delete, name='cliente_delete'),
    # Vistas CRUD Templates Trabajadores
    path('trabajadores/', trabajadores_list, name='trabajadores_list'),
    path('trabajadores/create', trabajadores_create, name='trabajadores_create'),
    path('trabajadores/update/<int:pk>', trabajadores_update, name='trabajadores_update'),
    path('trabajadores/delete/<int:pk>', trabajadores_delete, name='trabajadores_delete'),
    # Vistas CRUD Templates Horarios
    path('horario/', horarios_list, name='horarios_list'),
    path('horario/create', horarios_create, name='horarios_create'),
    path('horario/update/<int:pk>', horarios_update, name='horarios_update'),
    path('horario/delete/<int:pk>', horarios_delete, name='horarios_delete'),
    # Vistas CRUD Templates Citas
    path('citas/', citas_list, name='citas_list'),
    path('citas/create', citas_create, name='citas_create'),
    path('citas/update/<int:pk>', citas_update, name='citas_update'),
    path('citas/delete/<int:pk>', citas_delete, name='citas_delete'),
]