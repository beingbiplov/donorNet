# Generated by Django 2.2 on 2020-04-11 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0014_delete_donoraccept'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonorAccept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_accepted', models.BooleanField(default=False)),
                ('bloodrequest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.BloodRequest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
