# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='story',
            options={'verbose_name_plural': 'Stories'},
        ),
        migrations.AddField(
            model_name='story',
            name='story',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_stories', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='release_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.RemoveField(
            model_name='story',
            name='total_score',
        ),
        migrations.AddField(
            model_name='story',
            name='total_score',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
