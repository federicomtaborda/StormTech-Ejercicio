from statistics import mode
from django.contrib import admin

from App_Base.models import Cliente

from .models import *

# Register your models here.

admin.site.register(Cliente)

admin.site.register(Paquete)

admin.site.register(Motivo_Fallo)

class ItemInline(admin.StackedInline):
    model = Item
    extra = 0

class PlantillaAdmin(admin.ModelAdmin):
    inlines = [ItemInline]

admin.site.register(Plantilla, PlantillaAdmin)


admin.site.register(Item)

admin.site.register(Estado_Tracking)