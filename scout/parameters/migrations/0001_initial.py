# Generated by Django 5.0.3 on 2024-04-02 19:18

import django.contrib.postgres.fields
import parameters.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAgents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agents', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=2000), default=parameters.models.return_agents, size=None)),
                ('last_update', models.IntegerField(default=0)),
            ],
        ),
    ]
