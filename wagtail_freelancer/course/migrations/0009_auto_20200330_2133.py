# Generated by Django 2.0.9 on 2020-03-30 11:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_auto_20200329_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='HolidayCourseInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('student_keen', models.BooleanField(default=True)),
                ('is_student', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=250, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('amount_paid', models.DecimalField(decimal_places=2, default=10.0, max_digits=6, validators=[django.core.validators.MinValueValidator(1.0)])),
            ],
        ),
        migrations.DeleteModel(
            name='HolidayCourseContact',
        ),
    ]
