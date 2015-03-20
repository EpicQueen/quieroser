# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0002_step_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='number',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='step',
            unique_together=set([('track', 'number')]),
        ),
    ]
