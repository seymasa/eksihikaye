# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('parent', models.ForeignKey(to='stories.Genre', related_name='sub_genres', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('release_date', models.PositiveSmallIntegerField()),
                ('author', models.ForeignKey(related_name='posted_stories', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='liked_stories', null=True, to=settings.AUTH_USER_MODEL)),
                ('total_score', models.ManyToManyField(related_name='stories', to='stories.Genre')),
            ],
        ),
    ]
