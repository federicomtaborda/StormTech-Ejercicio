# Generated by Django 3.2 on 2022-05-21 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_Base', '0005_auto_20220521_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='motivo_fallo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Base.motivo_fallo', verbose_name='Motivo de Fallo'),
        ),
        migrations.AlterField(
            model_name='item',
            name='num_platilla',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Base.plantilla', verbose_name='N° Plantilla'),
        ),
    ]
