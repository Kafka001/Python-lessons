# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apppshka', '0003_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='comment_contenct',
            new_name='comment_content',
        ),
    ]
