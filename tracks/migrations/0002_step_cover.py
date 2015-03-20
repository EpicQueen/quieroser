# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='cover',
            field=models.ImageField(default='default.png', upload_to='step-cover/'),
            preserve_default=False,
        ),
    ]
