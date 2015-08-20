# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_auto_20150820_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='likes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, related_name='liked_stories'),
        ),
    ]
