# Generated by Django 5.0.6 on 2024-06-25 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_products_save'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='save',
        ),
    ]
