# Generated by Django 2.0.6 on 2018-10-18 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0005_auto_20181011_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='status',
            field=models.CharField(choices=[(1, '正常'), (2, '异常')], default=1, max_length=10, verbose_name='状态'),
        ),
    ]
