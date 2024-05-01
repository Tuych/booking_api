# Generated by Django 5.0.4 on 2024-04-30 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_booking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'active'), (2, 'cancel'), (3, 'book')], default=1),
        ),
    ]
