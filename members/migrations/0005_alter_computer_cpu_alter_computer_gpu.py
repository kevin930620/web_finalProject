# Generated by Django 4.2.7 on 2023-12-12 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_cputype_gpubrands_alter_computer_brand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='CPU',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='computer',
            name='GPU',
            field=models.CharField(max_length=255),
        ),
    ]
