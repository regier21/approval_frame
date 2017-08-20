# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('approval_polls', '0013_poll_is_suspended'),
    ]

    operations = [
        migrations.CreateModel(
            name='PollTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_text', models.CharField(max_length=100)),
                ('polls', models.ManyToManyField(to='approval_polls.Poll')),
            ],
        ),
    ]
