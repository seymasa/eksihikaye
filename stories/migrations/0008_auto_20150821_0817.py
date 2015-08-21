# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0007_story_scored_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='story_parent',
            field=models.ForeignKey(related_name='sub_story', to='stories.Story', blank=True, null=True),
        ),
    ]
