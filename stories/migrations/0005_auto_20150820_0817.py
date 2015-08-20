# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_auto_20150820_0805'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='parent',
            new_name='story_parent',
        ),
    ]
