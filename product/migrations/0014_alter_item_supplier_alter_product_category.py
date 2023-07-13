# Generated by Django 4.1.6 on 2023-07-13 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0002_supplier_slug'),
        ('product', '0013_remove_product_pcategory_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supplier_item', to='supplier.supplier'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='product_category', to='product.category'),
        ),
    ]