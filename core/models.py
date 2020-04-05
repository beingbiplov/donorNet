from django.db import models
# from django.utils import timezone
from datetime import date

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
    name= models.CharField( max_length=150)
    age = models.IntegerField()
    gender = models.CharField(max_length=50, choices=gender_choices)
    number = models.IntegerField()
    location = models.CharField( max_length=50)
    blood_group = models.CharField(max_length=10, choices=blood_choices)
    email = models.EmailField(max_length=254, blank=True, null= True)
    last_donated = models.DateField(default=date.today)
    
    is_18 = models.BooleanField()

    


    def __str__(self):
        return self.blood_group
    