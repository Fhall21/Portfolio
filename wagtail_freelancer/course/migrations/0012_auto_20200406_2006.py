# Generated by Django 2.0.9 on 2020-04-06 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_auto_20200402_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holidaycourseinterestdata',
            name='referee',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
