# Generated by Django 2.0 on 2017-12-13 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomstore', '0002_product_categories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelTable(
            name='category',
            table='categories',
        ),
        migrations.AlterModelTable(
            name='product',
            table='products',
        ),
    ]
