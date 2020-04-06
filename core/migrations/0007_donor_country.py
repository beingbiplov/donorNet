# Generated by Django 2.2 on 2020-04-06 05:04

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200405_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='country',
            field=django_countries.fields.CountryField(default='Nepal', max_length=2),
            preserve_default=False,
        ),
    ]
