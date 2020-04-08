# Generated by Django 2.2 on 2020-04-08 05:57

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0009_donor_can_donate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='phone_number',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\d{1,15}$')]),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(17), django.core.validators.MaxValueValidator(70)])),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=50)),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\d{1,15}$')])),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_donor', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
