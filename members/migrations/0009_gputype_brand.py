# Generated by Django 5.0 on 2023-12-12 06:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_alter_test_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='gputype',
            name='brand',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='members.gpubrands'),
        ),
    ]
