# Generated by Django 4.0.4 on 2022-07-07 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'product category', 'verbose_name_plural': 'product categories'},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name': 'product image', 'verbose_name_plural': 'products images'},
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]