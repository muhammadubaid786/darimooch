# Generated by Django 5.0.6 on 2024-06-24 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=60)),
                ('discription', models.TextField()),
                ('price', models.IntegerField()),
                ('category', models.CharField(max_length=60)),
            ],
        ),
    ]
