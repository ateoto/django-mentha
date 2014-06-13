# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentha', '0009_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='payee',
            name='regex',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='payee',
            name='fi_name',
        ),
    ]
