from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import User
from django.contrib import messages

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		r_email = request.POST['email']

		email_check = User.objects.filter(email=r_email)
		
		if not email_check:

			if form.is_valid():
				form.save()
			messages.info(request, f'Please log in to continue!')
			if 'register_donor' in request.POST:
				return redirect('core:add-donor-info')
			else:
				return redirect('core:add-patient-info')
		else:
			messages.info(request, f'The email address already has an account. Please log in or use a different email address')
			return redirect('register')

	else:
		form = RegisterForm()
	return render(request, 'register/register.html', {'form':form})
