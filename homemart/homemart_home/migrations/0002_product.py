# Generated by Django 3.1.5 on 2021-03-22 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homemart_home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('discription', models.TextField()),
                ('image', models.CharField(blank=True, max_length=5000, null=True)),
            ],
        ),
    ]
