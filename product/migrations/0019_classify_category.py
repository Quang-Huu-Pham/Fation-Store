# Generated by Django 4.1.4 on 2023-01-03 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_remove_classify_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='classify',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classifies', to='product.category'),
        ),
    ]
