from statistics import mode
from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['cliente_name','telefono','direccion','email','estado']
    search_fields=('cliente_name', 'estado')
    list_filter = ('estado',)
  
  
@admin.register(Paquete)
class PaqueteAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Tracking", {"fields": ["tracking"]}),
            ( "Datos de Paquete", 
                {"fields":['direccion_des', 'telefono_des', 'nombre_des'] }
            ),
            ( "Peso - Altura", 
                {"fields":['peso', 'altura'] }
            ),
            ( "Caracteristicas", 
                {"fields":['cliente', 'estado', 'tipo_paquete'] }
            )

    ]
    list_display = ['pk','tracking','direccion_des','telefono_des','cliente','tipo_paquete','estado']
    list_filter = ('tracking', 'estado')
    search_fields=('tracking', 'estado','cliente')
    list_display_links = ('cliente', 'pk')
    readonly_fields = ('tipo_paquete',)



class ItemInline(admin.StackedInline):
    model = Item
    extra = 0

@admin.register(Plantilla)
class PlantillaAdmin(admin.ModelAdmin):
    list_display = ['pk','posicion','fecha']
    list_filter = ('posicion','fecha')
    readonly_fields = ('fecha',)
    inlines = [ItemInline]
    ordering = ['fecha']
    actions = ['Cambiar_Estado']

def Cambiar_Estado(self, request, queryset):
    queryset = Paquete.objects.filter(estado=1).update(estado=2)

Cambiar_Estado.short_description = 'Pasar a Distribución'


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk','num_platilla','posicion','motivo_fallo']
    list_filter = ('motivo_fallo','posicion')
    search_fields=('num_platilla','posicion','motivo_fallo')


@admin.register(Estado_Tracking)
class Estado_TrackingAdmin(admin.ModelAdmin):
    list_display = ['estado_tracking']


admin.site.register(Motivo_Fallo)
