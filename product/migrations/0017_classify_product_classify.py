# Generated by Django 4.1.4 on 2023-01-03 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_remove_product_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classifies', to='product.category')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='classify',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classify', to='product.classify'),
        ),
    ]
