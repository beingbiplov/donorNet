# Generated by Django 2.2 on 2020-04-06 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_donor_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='is_18',
        ),
    ]
