from datetime import datetime

from django.db import models
# Create your models here.


## Clases Models ##
class Estado_Tracking(models.Model):
    estado_tracking = models.CharField(max_length=100, verbose_name="Estado")
    
    def __str__(self):
        return self.estado_tracking


class Motivo_Fallo(models.Model):
    motivo_fallo = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.motivo_fallo

class Cliente(models.Model):
    cliente_name = models.CharField(max_length=200, unique=True, verbose_name="Nombre de Cliente")
    telefono = models.CharField(max_length=15, null=False, blank=False, verbose_name="Teléfono")
    direccion = models.CharField(max_length=200, verbose_name="Direccón")
    email = models.EmailField(max_length=50, null=True, blank=True, verbose_name="Email")
    estado = models.BooleanField(default=True, verbose_name="Estado de Cliente")

    def __str__(self):
        return self.cliente_name
## ---end---- ##

class Paquete(models.Model):
    tracking = models.CharField(max_length=100, unique=True, verbose_name="N° Tracking")
    direccion_des = models.CharField(max_length=200, verbose_name="Dirección Destino")
    telefono_des = models.CharField(max_length=15, verbose_name="Teléfono")
    nombre_des = models.CharField(max_length=200, unique=True, verbose_name="Nombre Destino")
    peso = models.DecimalField(default=0.00, max_digits=5, decimal_places=2, verbose_name="Peso")
    altura =  models.DecimalField(default=0.00, max_digits=5, decimal_places=2, verbose_name="Altura")
    estado = models.ForeignKey(Estado_Tracking, on_delete=models.CASCADE, verbose_name="Estado")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    tipo_paquete = models.CharField(max_length=25)

    def __str__(self):
        return self.tracking

class Plantilla(models.Model):
    fecha = models.DateField(default=datetime.now)
    posicion = models.CharField(max_length=200)


class Item(models.Model):
    num_platilla = models.ForeignKey(Plantilla, on_delete=models.CASCADE)
    paquete = models.ManyToManyField(Paquete)
    posicion = models.CharField(max_length=150)
    Motivo_Fallo = models.ForeignKey(Motivo_Fallo, on_delete=models.CASCADE)









