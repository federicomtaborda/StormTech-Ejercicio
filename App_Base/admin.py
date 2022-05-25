from django.db.models import Q
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
    search_fields=('pk', 'posicion')
    readonly_fields = ('fecha',)
    inlines = [ItemInline]
    ordering = ['fecha']
    actions = ['Pasar_Distribucion']

    def Pasar_Distribucion(self, request, queryset):
        id_item = Item.pk
        for plantilla in queryset:
            #Paquete.objects.filter(Q(estado=1) & 
            #~Q(pk = Item.pk)).update(estado=2)
            #variable = Paquete.objects.filter(plantilla.pk)   
            print(plantilla.pk)
    Pasar_Distribucion.short_description = 'Pasar a Distribución'

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk','num_plantilla','posicion','motivo_fallo']
    list_filter = ('motivo_fallo','posicion')
    search_fields=('num_platilla','posicion','motivo_fallo')


@admin.register(Estado_Tracking)
class Estado_TrackingAdmin(admin.ModelAdmin):
    list_display = ['pk','estado_tracking']
    search_fields = ('estado_tracking',)
    ordering = ['pk']


admin.site.register(Motivo_Fallo)



## ---Admin Titulos---- ##
admin.site.site_header = "Sistema de Logistica"
admin.site.site_title = "Ejercicio"
admin.site.index_title = "Ejercicio StormTech"