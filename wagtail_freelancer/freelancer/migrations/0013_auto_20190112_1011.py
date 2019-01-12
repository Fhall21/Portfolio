# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-12 00:11
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('freelancer', '0012_auto_20190112_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancerpage',
            name='mission',
            field=wagtail.core.fields.StreamField([('mission', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock()), ('icon_link', wagtail.core.blocks.RawHTMLBlock()), ('img_required', wagtail.core.blocks.BooleanBlock(required=False)), ('icon_img', wagtail.images.blocks.ImageChooserBlock())]))], blank=True, null=True),
        ),
    ]
