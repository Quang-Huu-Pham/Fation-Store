# Generated by Django 4.1.4 on 2023-01-03 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='static/assets'),
        ),
    ]
