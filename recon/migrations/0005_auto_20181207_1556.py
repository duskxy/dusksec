# Generated by Django 2.0.6 on 2018-12-07 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recon', '0004_auto_20180909_2102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='suser',
            options={},
        ),
        migrations.AlterModelTable(
            name='sudata',
            table='sudata',
        ),
        migrations.AlterModelTable(
            name='surl',
            table='surl',
        ),
        migrations.AlterModelTable(
            name='suser',
            table='suser',
        ),
    ]