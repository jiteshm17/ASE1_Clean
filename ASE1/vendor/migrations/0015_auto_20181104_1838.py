# Generated by Django 2.1.2 on 2018-11-04 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0014_auto_20181104_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.TimeField(default=datetime.datetime(2018, 11, 4, 18, 38, 34, 142487)),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.TimeField(default=datetime.datetime(2018, 11, 4, 18, 38, 34, 142487)),
        ),
    ]
