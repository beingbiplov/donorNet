from django import forms
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField

class SearchDonorForm(forms.Form):
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

	country = CountryField(blank_label='select country').formfield()
	blood_group = forms.ChoiceField(required=True, choices=blood_choices)
	location = forms.CharField(required=True, max_length= 50, 
				widget = forms.TextInput(attrs={
					'name':'location',
					'placeholder': 'Enter location eg: Kathmandu'
					}) )
