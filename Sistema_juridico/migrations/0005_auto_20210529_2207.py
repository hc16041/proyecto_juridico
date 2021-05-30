# Generated by Django 2.1 on 2021-05-30 04:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema_juridico', '0004_auto_20210529_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipodeabogado',
            name='nombre',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('[a-zA-Z]+[ a-zA-Z-_]*$', message='Introduzca letras del alfabeto')]),
        ),
    ]
