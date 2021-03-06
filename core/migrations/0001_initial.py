# Generated by Django 2.2 on 2020-04-05 03:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=50)),
                ('number', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
                ('blood_group', models.CharField(choices=[('A+ve', 'A+ve'), ('A-ve', 'A-ve'), ('B+ve', 'B+ve'), ('B-ve', 'B-ve'), ('AB+ve', 'AB+ve'), ('AB-ve', 'AB-ve'), ('O+ve', 'O+ve'), ('O-ve', 'O-ve')], max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('last_donated', models.DateField(default=datetime.date.today)),
                ('is_18', models.BooleanField()),
            ],
        ),
    ]
