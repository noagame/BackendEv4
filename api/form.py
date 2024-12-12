from .models import *
from django import forms 
from django.contrib.auth.models import User

# --------- Formulario para Registro de Usuario ---------
class CustomUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']
        labels = {
            'username':'Nombre de Usuario',
            'email':'Correo Electrónico',
            'password':'Contraseña',
        }
        widgets = {
            'password': forms.PasswordInput(),
        }
# --------- Formulario para Clientes ---------
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'cliente_id': forms.NumberInput(),
            'edad': forms.NumberInput(),    
            'genero': forms.Select(),
            'is_active': forms.CheckboxInput(),
        }
        # Etiquetas de formulario
        labels = {
            'cliente_id': 'ID del Cliente',
            'edad': 'Edad',
            'nombre':'Nombre',
            'apellido':'Apellidos',
            'email':'Email',
            'genero': 'Género',
            'is_active': 'Activo',
        }
# -------- Formulario para trabajadores ---------
class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajadore
        fields = '__all__'
        widgets = {
            'job_id': forms.NumberInput(),
            'edad': forms.NumberInput(),
            'specialty':forms.Select(),
            'afiliacion':forms.Select(),
            'genero': forms.Select(),
            'active': forms.CheckboxInput(),
        }
        # Etiquetas de formulario
        labels = {
            'job_id': 'ID del Trabajador',
            'edad': 'Edad',
            'name':'Nombre',
            'apellido':'Apellidos',
            'email':'Email',
            'afiliacion':'Afiliación',
            'genero': 'Género',
            'is_active': 'Activo',
            'specialty': 'Especialidad'
        }
# -------- Formulario para Horas de Medico ---------
class HorarioForm(forms.ModelForm):
    class Meta:
        model = HorarioDisponible
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora_inicio': forms.TimeInput(attrs={'type': 'time'}),
            'hora_fin': forms.TimeInput(attrs={'type': 'time'}),
            'is_valid': forms.CheckboxInput(),
        }
        labels = {
            'trabajador':'Selecciona el Medico',
            'fecha':'Fecha Disponible',
            'hora_inicio': 'Hora Inicio',
            'hora_fin': 'Hora Fin',
            'is_valid':'Disponibilidad'
        }
# -------- Formulario para Citas entre Medico y Cliente en un Horario Disponible ---------
class CitasForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = '__all__'
        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'trabajador': forms.Select(attrs={'class': 'form-control'}),
            'dia': forms.Select(attrs={'class': 'form-control'}),
            }
        labels = {
            'usuario': 'Nombre del Paciente',
            'trabajador': 'Seleccione el Trabajador',
            'dia': 'Día de la Cita',
        }