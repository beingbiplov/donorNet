# Generated by Django 2.2 on 2020-04-05 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200405_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='location2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
