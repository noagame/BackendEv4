from django.contrib import admin
from .models import Cliente, Trabajadore, HorarioDisponible, Cita
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Trabajadore)
admin.site.register(HorarioDisponible)
admin.site.register(Cita)

