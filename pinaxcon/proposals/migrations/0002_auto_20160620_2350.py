# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='talkproposal',
            name='audience_level',
        ),
        migrations.AddField(
            model_name='talkproposal',
            name='materials_release',
            field=models.BooleanField(default=True, help_text=b"I allow Linux Australia to release any other material (such as slides) from presentations covered by this proposal, under the <a href='https://creativecommons.org/licenses/by-sa/3.0/au/deed.en'> Creative Commons Attribution-Share Alike Australia 3.0 Licence</a>"),
        ),
        migrations.AddField(
            model_name='talkproposal',
            name='target_audience',
            field=models.IntegerField(choices=[(1, b'User'), (2, b'Business'), (3, b'Community'), (4, b'Developer')], default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='talkproposal',
            name='recording_release',
            field=models.BooleanField(default=True, help_text=b"I allow Linux Australia to release any recordings of presentations covered by this proposal, under the <a href='https://creativecommons.org/licenses/by-sa/3.0/au/deed.en'> Creative Commons Attribution-Share Alike Australia 3.0 Licence</a>"),
        ),
    ]
