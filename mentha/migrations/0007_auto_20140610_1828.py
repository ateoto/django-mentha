# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentha', '0006_auto_20140610_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payee',
            name='fi_name',
            field=models.CharField(max_length=100, null=True, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(to_field='id', blank=True, to='mentha.Category', null=True),
        ),
        migrations.AlterField(
            model_name='payee',
            name='category',
            field=models.ForeignKey(to_field='id', blank=True, to='mentha.Category', null=True),
        ),
    ]
