# Generated by Django 2.1.2 on 2018-12-02 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0007_auto_20181202_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='qty',
        ),
        migrations.AddField(
            model_name='vendorqty',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vendor.Product'),
        ),
    ]