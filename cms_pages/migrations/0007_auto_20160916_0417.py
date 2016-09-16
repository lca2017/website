# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-16 04:17
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms_pages', '0006_auto_20160916_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('rich_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False))]),
        ),
        migrations.AlterField(
            model_name='newsindexpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('rich_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False))]),
        ),
        migrations.AlterField(
            model_name='newspage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('rich_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False))]),
        ),
    ]
