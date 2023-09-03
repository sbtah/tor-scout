# Generated by Django 4.2.4 on 2023-09-02 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.URLField(unique=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True)),
                ('created', models.IntegerField(blank=True, null=True)),
                ('website_map', models.JSONField()),
                ('description_tags', models.ManyToManyField(to='crawled.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=255, unique=True)),
                ('created', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True)),
                ('is_file', models.BooleanField(default=False)),
                ('number_of_references', models.IntegerField(blank=True, null=True)),
                ('last_visit', models.IntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('parrent_website', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crawled.website')),
            ],
        ),
    ]
