# Generated by Django 2.1 on 2021-05-16 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema_juridico', '0004_auto_20210516_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
    ]
