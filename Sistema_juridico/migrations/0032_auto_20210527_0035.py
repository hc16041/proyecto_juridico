# Generated by Django 2.1 on 2021-05-27 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema_juridico', '0031_usuario_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]