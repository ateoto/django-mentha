# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentha', '0005_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payee',
            name='category',
            field=models.ForeignKey(to='mentha.Category', blank=True, to_field='id'),
        ),
    ]
