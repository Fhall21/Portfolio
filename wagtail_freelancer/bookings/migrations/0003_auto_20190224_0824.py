# Generated by Django 2.0.9 on 2019-02-23 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20190224_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='day_time',
            field=models.DateTimeField(blank=True, unique=True),
        ),
    ]
