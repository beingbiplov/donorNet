from django.db import models
from django.utils import timezone
from datetime import date
from users.models import User
from django.core.validators import MaxValueValidator , MinValueValidator
from django.core.validators import RegexValidator
from django_countries.fields import CountryField
from django.urls import reverse

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
    phone_number = models.CharField(max_length=15, validators=[RegexValidator(r'^\d{1,15}$')])
    location1 = models.CharField( max_length=50)
    location2 = models.CharField( max_length=50, null=True, blank=True)
    country = CountryField(blank_label='(select country)')
    blood_group = models.CharField(max_length=10, choices=blood_choices)    
    last_donated = models.DateField(null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)

    can_donate = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.full_name} : {self.blood_group}'
    
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name= models.CharField( max_length=150)
    age = models.IntegerField(validators=[MinValueValidator(17), MaxValueValidator(70)])
    gender = models.CharField(max_length=50, choices=gender_choices)
    phone_number = models.CharField(max_length=15, validators=[RegexValidator(r'^\d{1,15}$')])
    
    date_joined = models.DateTimeField(default=timezone.now)

    is_donor = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.full_name} : {self.blood_group}'

class BloodRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=10, choices=blood_choices)
    phone_number = models.CharField(max_length=15, validators=[RegexValidator(r'^\d{1,15}$')])
    country = CountryField(blank_label='(select country)')
    location1 = models.CharField( max_length=50)
    location2 = models.CharField( max_length=50, null=True, blank=True)
    required_on = models.DateTimeField(blank=False, null=False)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('core:send-request',kwargs={'pk':self.pk})
    
    def __str__(self):
        return f'{self.country}-{self.location1} : {self.blood_group}'


class DonorRequest(models.Model):
    bloodrequest = models.ForeignKey(BloodRequest, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)

    def __Str__(self):
        return f'{self.bloodrequest.blood_group}'