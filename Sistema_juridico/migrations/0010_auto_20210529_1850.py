# Generated by Django 2.1.15 on 2021-05-30 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sistema_juridico', '0009_auto_20210529_1848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caso',
            old_name='tipo_pago',
            new_name='pago_caso',
        ),
    ]
