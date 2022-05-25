from datetime import datetime
from tabnanny import verbose

from django.db import models
# Create your models here.


## Clases Models ##
class Estado_Tracking(models.Model):
    estado_tracking = models.CharField(max_length=100, verbose_name="Estado")

    class Meta:
        verbose_name = "Tracking"
        verbose_name_plural = "Estado Tracking"
    
    def __str__(self):
        return self.estado_tracking
## ---end---- ##



## Motivo Fallo Models ##
class Motivo_Fallo(models.Model):
    motivo_fallo = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Fallo"
        verbose_name_plural = "Motivo de Fallo"

    def __str__(self):
        return self.motivo_fallo

## ---end---- ##


## ---Cliente Models---- ##
class Cliente(models.Model):
    cliente_name = models.CharField(max_length=200, unique=True, verbose_name="Nombre de Cliente")
    telefono = models.CharField(max_length=15, null=False, blank=False, verbose_name="Teléfono")
    direccion = models.CharField(max_length=200, verbose_name="Direccón")
    email = models.EmailField(max_length=50, null=True, blank=True, verbose_name="Email")
    estado = models.BooleanField(default=True, verbose_name="Estado de Cliente")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.cliente_name

## ---end---- ##



## Paquete Models ##
class Paquete(models.Model):
    tracking = models.CharField(max_length=100, unique=True, verbose_name="N° Tracking")
    direccion_des = models.CharField(max_length=200, verbose_name="Dirección Destino")
    telefono_des = models.CharField(max_length=15, verbose_name="Teléfono")
    nombre_des = models.CharField(max_length=200, unique=True, verbose_name="Nombre Destino")
    peso = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name="Peso")
    altura =  models.DecimalField(default=0.00, max_digits=5, decimal_places=2, verbose_name="Altura")
    estado = models.ForeignKey(Estado_Tracking, on_delete=models.CASCADE, verbose_name="Estado")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    tipo_paquete = models.CharField(max_length=25, editable=False )

    def save(self, **kwargs):
        peso = self.peso
        if peso > 0 and peso < 1000:
            self.tipo_paquete = "P"
        if peso >= 1000 and peso < 3000:
            self.tipo_paquete = "M"
        if peso >= 3000:
            self.tipo_paquete = "G"
        return super(Paquete, self).save()


    class Meta:
        verbose_name = "Paquete"
        verbose_name_plural = "Paquetes"


    def __str__(self):
        return self.tracking
## ---end---- ##



## Plantilla Models ##
class Plantilla(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    posicion = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Plantilla"
        verbose_name_plural = "Plantilla"
        ordering = ['-fecha']

    def __str__(self):
        return 'Plantilla n°: {}'.format(self.pk)
## ---end---- ##



## Item Models ##
class Item(models.Model):
    num_plantilla = models.ForeignKey(Plantilla, on_delete=models.CASCADE, verbose_name="N° Plantilla")
    paquete = models.ManyToManyField(Paquete)
    posicion = models.CharField(max_length=150)
    motivo_fallo = models.ForeignKey(Motivo_Fallo, on_delete=models.CASCADE, verbose_name="Motivo de Fallo")

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items de Plantilla"
    
    def __str__(self):
        return '{}'.format(self.num_plantilla.pk)

## ---end---- ##



