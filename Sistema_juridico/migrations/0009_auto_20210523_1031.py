# Generated by Django 2.1.15 on 2021-05-23 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema_juridico', '0008_auto_20210517_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abogado',
            name='Tipo_de_abogado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sistema_juridico.TipoDeAbogado', verbose_name='Tipo De Abogado'),
        ),
    ]
