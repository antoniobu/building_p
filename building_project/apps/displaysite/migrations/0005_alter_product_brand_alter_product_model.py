# Generated by Django 5.0 on 2024-05-31 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('displaysite', '0004_product_brand_product_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(default='Unknown Brand', max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='model',
            field=models.CharField(default='Unknown Model', max_length=255),
        ),
    ]