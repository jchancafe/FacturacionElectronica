# Generated by Django 2.0.6 on 2018-09-18 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0034_resumencab_tipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resumencab',
            name='tipo',
        ),
        migrations.AddField(
            model_name='resumencab',
            name='tipodoc_comprobante',
            field=models.CharField(blank=True, db_column='TIPODOC_COMPROBANTE', max_length=2, null=True),
        ),
    ]
