# Generated by Django 2.0.6 on 2018-09-06 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0026_auto_20180905_1711'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='resumencab',
            unique_together={('tipo_resumen', 'numdoc_resumen', 'numser_resumen')},
        ),
    ]
