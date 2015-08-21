# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0008_auto_20150821_0817'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='genres',
            field=models.ManyToManyField(to='stories.Genre', related_name='stories', blank=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='parent',
            field=models.ForeignKey(null=True, related_name='sub_genres', to='stories.Genre', blank=True),
        ),
    ]
