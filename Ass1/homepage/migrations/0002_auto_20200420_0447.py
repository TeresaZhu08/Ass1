# Generated by Django 3.0.4 on 2020-04-20 04:47

import asgiref.local
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=0),
        ),
    ]
