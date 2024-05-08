from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

# Create your models here.
class Cuota(models.Model):
    id_cuota = models.AutoField(primary_key=True)
    nombre_cuota = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_cuota

class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    rut_persona = models.CharField(max_length=10)
    nombre_persona = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_persona
    
class CuotaPersona(models.Model):
    id_cuota_persona = models.AutoField(primary_key=True)
    monto_cuota = models.IntegerField()
    fecha = models.DateField()
    estado = models.BooleanField()
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE) 
    cuota = models.ForeignKey(Cuota, on_delete=models.CASCADE) 
    def __str__(self):
        return f"{self.persona.nombre_persona} - {self.cuota.nombre_cuota} - {self.estado}"