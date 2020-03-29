# Generated by Django 2.0.9 on 2020-03-29 00:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_auto_20200327_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holidaycoursecontact',
            name='amount_paid',
            field=models.DecimalField(decimal_places=2, default=180.0, max_digits=6, validators=[django.core.validators.MinValueValidator(60.0)]),
        ),
    ]
