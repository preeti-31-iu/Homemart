# Generated by Django 3.1.5 on 2021-03-22 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homemart_home', '0003_product_cartid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]
