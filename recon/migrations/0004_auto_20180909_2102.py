# Generated by Django 2.0.6 on 2018-09-09 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recon', '0003_auto_20180909_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sudata',
            name='uid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recon.Surl', verbose_name='域名'),
        ),
    ]