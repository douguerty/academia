# Generated by Django 2.0.7 on 2018-07-06 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20180705_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='altura',
            field=models.CharField(blank=True, max_length=6, verbose_name='Altura em cm'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='peso',
            field=models.CharField(blank=True, max_length=7, verbose_name='Peso em kg'),
        ),
    ]
