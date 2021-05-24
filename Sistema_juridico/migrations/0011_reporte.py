# Generated by Django 2.1.2 on 2021-05-24 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema_juridico', '0010_auto_20210519_0003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('codigo_reporte', models.IntegerField(primary_key=True, serialize=False)),
                ('estado_cliente', models.IntegerField(choices=[('P', 'En Proceso'), ('F', 'Finalizado')], default=0)),
                ('codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sistema_juridico.Caso', verbose_name='Id caso')),
                ('dui_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sistema_juridico.Cliente', verbose_name='Id Cliente')),
                ('nombre_abogado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sistema_juridico.Abogado', verbose_name='Id Abogado')),
                ('tipo_de_proceso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sistema_juridico.TipoDeProceso')),
            ],
            options={
                'verbose_name': 'Reporte',
                'verbose_name_plural': 'Reportes',
            },
        ),
    ]