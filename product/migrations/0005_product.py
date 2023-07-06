# Generated by Django 4.1.6 on 2023-07-06 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0004_alter_brand_options_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Product Name')),
                ('slug', models.SlugField(max_length=255, verbose_name='Product Slug')),
                ('description', models.TextField(verbose_name='Product Description')),
                ('type', models.CharField(max_length=20, null=True, verbose_name='Product Type')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(to='product.category')),
                ('created_by', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_creator', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '3. Product',
                'db_table': 'product',
            },
        ),
    ]
