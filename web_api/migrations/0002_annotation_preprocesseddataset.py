# Generated by Django 2.2.5 on 2020-11-03 18:04

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreprocessedDataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ready', models.BooleanField(default=False)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_api.Dataset')),
            ],
        ),
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boxes', django.contrib.postgres.fields.jsonb.JSONField()),
                ('preprocessed_dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_api.Dataset')),
            ],
        ),
    ]
