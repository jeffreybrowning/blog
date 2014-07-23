# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20140720_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='tags',
            field=models.ManyToManyField(to=b'blog.Tag', blank=True),
        ),
    ]
