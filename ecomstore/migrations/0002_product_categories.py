# Generated by Django 2.0 on 2017-12-13 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='ecomstore.Category'),
        ),
    ]
