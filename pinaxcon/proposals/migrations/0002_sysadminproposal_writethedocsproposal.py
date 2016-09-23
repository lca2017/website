# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-21 10:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_proposals', '0001_initial'),
        ('proposals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SysAdminProposal',
            fields=[
                ('proposalbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='symposion_proposals.ProposalBase')),
                ('target_audience', models.IntegerField(choices=[(1, b'User'), (2, b'Business'), (3, b'Community'), (4, b'Developer')])),
                ('recording_release', models.BooleanField(default=True, help_text=b"I allow Linux Australia to release any recordings of presentations covered by this proposal, under the <a href='https://creativecommons.org/licenses/by-sa/3.0/au/deed.en'> Creative Commons Attribution-Share Alike Australia 3.0 Licence</a>")),
                ('materials_release', models.BooleanField(default=True, help_text=b"I allow Linux Australia to release any other material (such as slides) from presentations covered by this proposal, under the <a href='https://creativecommons.org/licenses/by-sa/3.0/au/deed.en'> Creative Commons Attribution-Share Alike Australia 3.0 Licence</a>")),
                ('talk_format', models.IntegerField(choices=[(1, b'Long Presentation (45 min)'), (2, b'Short Presentation (20 min)'), (3, b'Lightning Talk (5 min)')])),
            ],
            options={
                'verbose_name': 'System Administration Miniconf Proposal',
            },
            bases=('symposion_proposals.proposalbase',),
        ),
        migrations.CreateModel(
            name='WriteTheDocsProposal',
            fields=[
                ('proposalbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='symposion_proposals.ProposalBase')),
                ('target_audience', models.IntegerField(choices=[(1, b'User'), (2, b'Business'), (3, b'Community'), (4, b'Developer')])),
                ('recording_release', models.BooleanField(default=True, help_text=b"I allow Linux Australia to release any recordings of presentations covered by this proposal, under the <a href='https://creativecommons.org/licenses/by-sa/3.0/au/deed.en'> Creative Commons Attribution-Share Alike Australia 3.0 Licence</a>")),
                ('materials_release', models.BooleanField(default=True, help_text=b"I allow Linux Australia to release any other material (such as slides) from presentations covered by this proposal, under the <a href='https://creativecommons.org/licenses/by-sa/3.0/au/deed.en'> Creative Commons Attribution-Share Alike Australia 3.0 Licence</a>")),
                ('talk_format', models.IntegerField(choices=[(1, b'Long Presentation (40 min)'), (2, b'Short Presentation (20 min)')])),
            ],
            options={
                'verbose_name': 'WriteThe Docs Miniconf Proposal',
            },
            bases=('symposion_proposals.proposalbase',),
        ),
    ]
