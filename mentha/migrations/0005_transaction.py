# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentha', '0004_payee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account', models.ForeignKey(to='mentha.Account', to_field='id')),
                ('date', models.DateField(auto_now_add=True)),
                ('amount', models.DecimalField(max_digits=20, decimal_places=2)),
                ('transaction_type', models.PositiveSmallIntegerField(default=0, choices=[(0, b'Debit'), (1, b'Credit')])),
                ('payee', models.ForeignKey(to='mentha.Payee', to_field='id')),
                ('category', models.ForeignKey(to='mentha.Category', blank=True, to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
