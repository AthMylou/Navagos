# Generated by Django 5.0.4 on 2024-06-17 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('navagos_main', '0004_category_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='active',
        ),
    ]
