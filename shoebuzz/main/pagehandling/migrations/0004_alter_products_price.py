# Generated by Django 4.0.4 on 2022-06-16 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagehandling', '0003_alter_products_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.TextField(),
        ),
    ]
