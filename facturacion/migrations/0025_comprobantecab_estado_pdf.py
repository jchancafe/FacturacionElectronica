# Generated by Django 2.0.6 on 2018-09-05 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0024_auto_20180905_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='comprobantecab',
            name='estado_pdf',
            field=models.CharField(blank=True, choices=[('01', 'POR GENERAR'), ('02', 'GENERADO')], db_column='ESTADO_PDF', default='01', max_length=2, null=True),
        ),
    ]
