# Generated by Django 5.0.6 on 2024-07-06 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeimage',
            name='image',
            field=models.ImageField(upload_to='media', verbose_name='Изображения'),
        ),
    ]
