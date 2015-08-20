# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_story_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='parent',
            field=models.ForeignKey(to='stories.Story', related_name='sub_story', null=True),
        ),
    ]
