# Generated by Django 3.0 on 2020-01-16 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bestbonus', '0005_auto_20191201_0517'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bonus',
        ),
        migrations.DeleteModel(
            name='Suplier',
        ),
    ]