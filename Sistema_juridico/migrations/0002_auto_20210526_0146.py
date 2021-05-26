# Generated by Django 2.1 on 2021-05-26 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema_juridico', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caso',
            name='audiencia',
        ),
        migrations.RemoveField(
            model_name='caso',
            name='pago',
        ),
        migrations.RemoveField(
            model_name='formadepago',
            name='tipo',
        ),
        migrations.AddField(
            model_name='caso',
            name='tipo_pago',
            field=models.IntegerField(choices=[(0, 'Contado'), (1, 'Credito')], default=0),
        ),
        migrations.AddField(
            model_name='formadepago',
            name='fecha_fin_credito',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='caso',
            name='estado',
            field=models.IntegerField(choices=[('P', 'En Proceso'), ('F', 'Finalizado')], default=0),
        ),
    ]
