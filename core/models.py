from django.db import models
from django.utils import timezone
from datetime import date
from users.models import User
from django.core.validators import MaxValueValidator , MinValueValidator
from django.core.validators import RegexValidator
from django_countries.fields import CountryField

# Create your models here.
blood_choices = [
        ('A+ve', 'A+ve'),
        ('A-ve', 'A-ve'),
        ('B+ve', 'B+ve'),
        ('B-ve', 'B-ve'),
        ('AB+ve', 'AB+ve'),
        ('AB-ve', 'AB-ve'),
        ('O+ve', 'O+ve'),
        ('O-ve', 'O-ve'),
        ]

gender_choices = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others')
]

class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name= models.CharField( max_length=150)
    age = models.IntegerField(validators=[MinValueValidator(17), MaxValueValidator(70)])
    gender = models.CharField(max_length=50, choices=gender_choices)
    phone_number = models.CharField(max_length=15, validators=[RegexValidator(r'^\d{1,10}$')])
    location1 = models.CharField( max_length=50)
    location2 = models.CharField( max_length=50, null=True, blank=True)
    country = CountryField(blank_label='(select country)')
    blood_group = models.CharField(max_length=10, choices=blood_choices)    
    last_donated = models.DateField(null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)

    is_18 = models.BooleanField()
    
    def __str__(self):
        return f'{self.full_name} : {self.blood_group}'
    