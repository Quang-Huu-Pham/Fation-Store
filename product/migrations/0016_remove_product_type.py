# Generated by Django 4.1.4 on 2023-01-03 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_alter_product_type_delete_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='type',
        ),
    ]