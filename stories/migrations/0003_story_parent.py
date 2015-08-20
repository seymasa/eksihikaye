# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_auto_20150820_0657'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='parent',
            field=models.ForeignKey(default=2, related_name='sub_story', to='stories.Story'),
            preserve_default=False,
        ),
    ]
