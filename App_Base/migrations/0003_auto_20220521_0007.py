# Generated by Django 3.2.12 on 2022-05-21 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Base', '0002_alter_plantilla_fecha'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='estado_tracking',
            options={'verbose_name': 'Tracking', 'verbose_name_plural': 'Estado Tracking'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Item', 'verbose_name_plural': 'Items de Plantilla'},
        ),
        migrations.AlterModelOptions(
            name='motivo_fallo',
            options={'verbose_name': 'Fallo', 'verbose_name_plural': 'Motivo de Fallo'},
        ),
        migrations.AlterModelOptions(
            name='paquete',
            options={'verbose_name': 'Paquete', 'verbose_name_plural': 'Paquetes'},
        ),
        migrations.AlterModelOptions(
            name='plantilla',
            options={'ordering': ['-fecha'], 'verbose_name': 'Plantilla', 'verbose_name_plural': 'Plantilla'},
        ),
        migrations.AlterField(
            model_name='paquete',
            name='tipo_paquete',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
