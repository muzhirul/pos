# Generated by Django 4.1.6 on 2023-07-11 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_alter_item_options_remove_product_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pcategory',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='product.category'),
        ),
        migrations.DeleteModel(
            name='Productcategory',
        ),
    ]
