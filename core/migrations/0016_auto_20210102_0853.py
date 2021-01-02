# Generated by Django 2.2 on 2021-01-02 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_donoraccept'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='last_donated',
        ),
        migrations.AddField(
            model_name='donor',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='donor',
            name='verification_document',
            field=models.ImageField(default='default.jpeg', help_text='Upload image of document to verify your blood group.(eg, license, Donation card etc.', upload_to='verification_document'),
            preserve_default=False,
        ),
    ]