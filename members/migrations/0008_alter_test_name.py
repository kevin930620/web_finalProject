# Generated by Django 5.0 on 2023-12-12 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_alter_computer_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='name',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
