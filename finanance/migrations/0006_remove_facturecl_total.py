# Generated by Django 4.0.6 on 2023-01-30 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finanance', '0005_remove_facturefr_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facturecl',
            name='Total',
        ),
    ]
