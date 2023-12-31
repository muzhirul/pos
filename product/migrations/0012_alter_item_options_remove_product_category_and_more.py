# Generated by Django 4.1.6 on 2023-07-11 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_item_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-created_by'], 'verbose_name': '4. Item'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='product.category'),
        ),
        migrations.CreateModel(
            name='Productcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='pcategory',
            field=models.ManyToManyField(through='product.Productcategory', to='product.category'),
        ),
    ]
