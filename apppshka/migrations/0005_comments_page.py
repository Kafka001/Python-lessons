# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apppshka', '0004_auto_20151207_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='page',
            field=models.ForeignKey(blank=True, to='apppshka.App_new', null=True),
        ),
    ]
