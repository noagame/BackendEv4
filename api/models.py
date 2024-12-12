from django.db import models

#--------------------Modelo Cliente---------------------
class Cliente(models.Model):
    GENERO_CHOICES= [
        ('Masculino','Masculino'),
        ('Femenino','Femenino')
    ]
    cliente_id = models.AutoField(primary_key=True)
    edad = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=25, unique=True)
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES)
    is_active = models.BooleanField(default=True)
    ciudad = models.ForeignKey()
    # ----------------Fidelizacion----------------------
    # Uso de tiempo para saber cuando se creo el cliente

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ID: {self.cliente_id} Usuario: {self.nombre} Creado: {self.created_at} Activo: {self.is_active}"

#--------------------Modelo Medicos---------------------
class Trabajadore(models.Model):
    GENERO_CHOICES= [
        ('Masculino','Masculino'),
        ('Femenino','Femenino')
    ]
    SPECIALTY_CHOICES = [
        ('Medicina Interna','Médico Internista'),
        ('Cardiología','Cardiólogo'),
        ('Neumología','Neumólogo'),
        ('Endocrinología','Endocrinólogo'),
        ('Gastroenterología','Gastroenterólogo'),
        ('Hematología','Hematólogo'),
        ('Inmunología','Inmunólogo'),
        ('Reumatología','Reumatólogo'),
        ('Nefrología','Nefrólogo'),
        ('Oncología','Oncólogo'),
        ('Pediatría','Pediatra'),
        ('Psiquiatría','Psiquiatra'),
        ('Dermatología','Dermatólogo'),
        ('Neurología','Neurólogo')
    ]
    AFILIACION_CHOICE = [
        ('Fonasa','fonasa'),
        ('Isapre','isapre'),
        ('Ambos','ambos')
    ]
    job_id = models.AutoField(primary_key=True)
    edad = models.PositiveSmallIntegerField(default=0)
    name = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    email = models.EmailField(max_length=25, unique=True)
    specialty = models.CharField(max_length=20, choices=SPECIALTY_CHOICES, default='Ninguno') # Escoger Especialidad
    afiliacion = models.CharField(max_length=20, choices=AFILIACION_CHOICE, default='Ninguno') # Escoger Afiliacion
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES, default='Ninguno')
    is_active = models.BooleanField(default=True)

    # ----------------Fidelizacion-----------------------
    # Uso de tiempo para saber cuando se creo el usuario

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ID: {self.job_id} Doctor: {self.name} {self.apellido} Especialidad: {self.specialty} Creacion: {self.created_at}"

# --------------------Modelo de horarios------------------
class HorarioDisponible(models.Model):
    DAYS_CHOICES = [
        ('Lunes','Lunes'),
        ('Martes','Martes'),
        ('Miercoles','Miercoles'),
        ('Jueves','Jueves'),
        ('Viernes','Viernes'),
    ]
    trabajador = models.ForeignKey(Trabajadore, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=DAYS_CHOICES, default='Ninguno')
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.trabajador.name} {self.trabajador.apellido} - {self.day} - {self.hora_inicio} - {self.hora_fin}"
    
# ---------------------Modelo Citas ------------------------
class Cita(models.Model):
    usuario = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    trabajador = models.ForeignKey(Trabajadore, on_delete=models.CASCADE)
    dia = models.ForeignKey(HorarioDisponible, on_delete=models.CASCADE, default='None')
    confirmada = models.BooleanField(default=False)

    def __str__(self):
        return f"Cita {self.usuario.apellido} - {self.trabajador.apellido} el {self.dia.day}"

# ---------------------Modelo Ciudades ------------------------
class Ciudades(models.Model):
    CITY_CHOICES = [
        ('Angol','Angol'),
        ('Temuco','Temuco'),
        ('Padre de las Casas','Padre de las Casas'),
        ('Freire','Freire'),
        ('Pucon','Pucon')
    ]
    nombre= models.CharField(max_length=30, choices=CITY_CHOICES, default='none')