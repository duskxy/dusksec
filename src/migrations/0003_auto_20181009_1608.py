# Generated by Django 2.0.6 on 2018-10-09 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_asset'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asset',
            options={'verbose_name': 'src资产', 'verbose_name_plural': 'src资产'},
        ),
        migrations.AlterModelTable(
            name='asset',
            table='asset',
        ),
    ]
