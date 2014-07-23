# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20140720_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='author',
            field=models.CharField(default='Jeffrey Browning', max_length=50),
            preserve_default=False,
        ),
    ]
