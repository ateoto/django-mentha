# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('balance', models.DecimalField(max_digits=20, decimal_places=2)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id', editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
