import csv

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

# Manejo de errores
from django.db import IntegrityError
# Decoradores
from django.contrib.auth.decorators import login_required
# Formularios
from .form import *
# Librerias de Django Rest Framework
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
# Modelos 
from .models import *
# Serializadores
from .serializers import *

# --------------- Home ---------------------
def home(request):
    return render(request,'home.html')

# Vista Registro
def signup(request):
    if request.method == 'GET':
        return render(request, 'sign/signup.html', {"form": CustomUserForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'sign/signup.html', {"form": CustomUserForm, "error": "Este usuario ya existe."})

        return render(request, 'sign/signup.html', {"form": CustomUserForm, "error": "Las contraseñas no coinciden."})

# Vista Login
def signin(request):
    if request.method == 'GET':
        return render(request, 'sign/signin.html', {'form': AuthenticationForm})
    else:
        user = authenticate( request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'sign/signin.html', {'form':AuthenticationForm, 'error':'El usuario no existe'})
        
        login(request, user)
        return redirect('home')
# Funcionalidad Logout
@login_required
def signout(request):
    logout(request)
    return redirect('home')

# ---------------------- CRUD Clientes ----------------------------
# Listar todos los clientes
@login_required
def cliente_list(request):
    clientes = Cliente.objects.all()  # Consulta para obtener todos los clientes
    return render(request, 'clientes/list.html', {'clientes': clientes})

# Crear un nuevo cliente
@login_required
def cliente_create(request):
    form = ClienteForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('cliente_list')
    return render(request, 'clientes/form.html', {'form': form, 'title': 'Agregar Cliente'})

# Editar un cliente existente
@login_required
def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('cliente_list')
    return render(request, 'clientes/form.html', {'form': form, 'title': 'Editar Cliente'})

# Eliminar un cliente
@login_required
def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'clientes/delete.html', {'cliente': cliente})

# ---------------------- CRUD Trabajadores ----------------------------
# Listar todos los Trabajadores
@login_required
def trabajadores_list(request):
    trabajadores = Trabajadore.objects.all()  # Consulta para obtener todos los clientes
    return render(request, 'trabajadores/list.html', {'trabajadores': trabajadores})

# Crear un nuevo Trabajadores
@login_required
def trabajadores_create(request):
    form = TrabajadorForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('trabajadores_list')
    return render(request, 'trabajadores/form.html', {'form': form, 'title': 'Agregar Trabajador'})

# Editar un Trabajadores existente
@login_required
def trabajadores_update(request, pk):
    trabajadores = get_object_or_404(Trabajadore, pk=pk)
    form = TrabajadorForm(request.POST or None, instance=trabajadores)
    if form.is_valid():
        form.save()
        return redirect('trabajadores_list')
    return render(request, 'trabajadores/form.html', {'form': form, 'title': 'Editar Trabajador'})

# Eliminar un trabajador
@login_required
def trabajadores_delete(request, pk):
    trabajadores = get_object_or_404(Trabajadore, pk=pk)
    if request.method == 'POST':
        trabajadores.delete()
        return redirect('trabajadores_list')
    return render(request, 'trabajadores/delete.html', {'trabajadores': trabajadores})

# ---------------------- CRUD Horarios ----------------------------
# Listar todos los Horarios
@login_required
def horarios_list(request):
    horarios = HorarioDisponible.objects.all()  # Consulta para obtener todos los horarios
    return render(request, 'horarios/list.html', {'horarios': horarios})

# Crear un nuevo Horarios
def horarios_create(request):
    form = HorarioForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('horarios_list')
    return render(request, 'horarios/form.html', {'form': form, 'title': 'Agregar Horarios'})

# Editar un Horario existente
@login_required
def horarios_update(request, pk):
    horarios = get_object_or_404(HorarioDisponible, pk=pk)
    form = HorarioForm(request.POST or None, instance=horarios)
    if form.is_valid():
        form.save()
        return redirect('horarios_list')
    return render(request, 'horarios/form.html', {'form': form, 'title': 'Editar Horarios'})

# Eliminar un horario
@login_required
def horarios_delete(request, pk):
    horarios = get_object_or_404(HorarioDisponible, pk=pk)
    if request.method == 'POST':
        horarios.delete()
        return redirect('horarios_list')
    return render(request, 'horarios/delete.html', {'horarios': horarios})

# ---------------------- CRUD Citas ----------------------------
# ---------------- Templates ----------------
# Listar todos las Citas
@login_required
def citas_list(request):
    citas = Cita.objects.all()  # Consulta para obtener todos los clientes
    return render(request, 'citas/list.html', {'citas': citas})

# Crear un nueva Citas
def citas_create(request):
    form = CitasForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('citas_list')
    return render(request, 'citas/form.html', {'form': form, 'title': 'Agregar Cita'})

# Editar una Cita existente
@login_required
def citas_update(request, pk):
    citas = get_object_or_404(Cita, pk=pk)
    form = CitasForm(request.POST or None, instance=citas)
    if form.is_valid():
        form.save()
        return redirect('citas_list')
    return render(request, 'citas/form.html', {'form': form, 'title': 'Editar Citas'})

# Eliminar una Cita
@login_required
def citas_delete(request, pk):
    citas = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        citas.delete()
        return redirect('citas_list')
    return render(request, 'citas/delete.html', {'citas': citas})
# ---------------- API ----------------
# Configuración de filtrado especificando los campos en filterset_fields
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all() #Todos los registros de clientes
    serializer_class = ClienteSerializer #Serializador que se usa para la vista
    filter_backends = [DjangoFilterBackend] #Configuramos el backend de filtros
    filterset_fields = ['genero', 'active', 'created_at'] #Campos filtrables

class TrabajadorViewSet(viewsets.ModelViewSet):
    queryset = Trabajadore.objects.all()
    serializer_class = TrabajadorSerializer
    filter_backends = [DjangoFilterBackend] #Configuramos el backend de filtros
    filterset_fields = ['name','specialty','afiliacion'] #Campos filtrables

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = HorarioDisponible.objects.all()
    serializer_class = HorarioDisponibleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['trabajador', 'day']

class CitasViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitasSerializer
class CiudadesViewSey(viewsets.ModelViewSet):
    queryset = Ciudades.objects.all()
    serializer_class = CiudadesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre']

# Exportaciones CSV 
def export_Clientes(request):
    pass
def export_Trabajadores(request):
    pass
def export_