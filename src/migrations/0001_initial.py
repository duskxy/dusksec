# Generated by Django 2.0.6 on 2018-10-07 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Src',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=20, unique=True, verbose_name='src公司')),
                ('url', models.URLField(verbose_name='src网址')),
            ],
        ),
    ]