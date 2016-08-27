# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('votes', models.IntegerField(default=0)),
                ('candidate', models.ForeignKey(to='elections.Candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('area', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='poll',
            field=models.ForeignKey(to='elections.Poll'),
        ),
    ]
