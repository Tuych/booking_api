# Generated by Django 5.0.4 on 2024-04-30 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stadiums', '0002_stadium_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stadiumimage',
            name='is_main',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
