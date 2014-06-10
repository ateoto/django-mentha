# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mentha', '0003_budget'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('fi_name', models.CharField(max_length=100, editable=False, blank=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id', editable=False)),
                ('category', models.ForeignKey(to='mentha.Category', to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
