# Generated by Django 4.2.2 on 2023-07-10 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YokoCino', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cuerpo',
            field=models.TextField(max_length=1000),
        ),
    ]
