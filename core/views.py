from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView
from .models import Donor
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import SearchDonorForm


def index(request):
	form = SearchDonorForm
	return render(request, 'core/index.html', {'form': form})


class addDonnorInfo(LoginRequiredMixin, UserPassesTestMixin, CreateView):

	

	model = Donor
	fields = ['full_name','age', 'gender', 'phone_number', 'blood_group', 'country', 'location1', 'location2','last_donated','is_18']
	template_name = 'core/createdonorprofile.html'
	success_url = reverse_lazy('core:index')


	def get_form(self):
		'''add date picker in forms'''
		from django.forms.widgets import SelectDateWidget
		form = super(addDonnorInfo, self).get_form()
		form.fields['last_donated'].widget = SelectDateWidget(years=range(2019, 2021))
		
		return form
		
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)


	def test_func(self):

		check_user_info = Donor.objects.filter(user=self.request.user)

		if not check_user_info:
			return True
		return False


class updateDonnorInfo(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Donor
	fields = ['full_name','age', 'gender', 'phone_number', 'blood_group', 'location1', 'location2','last_donated','is_18']
	template_name = 'core/updatedonorinfo.html'
	success_url = reverse_lazy('core:index')

	def test_func(self):
		
		check_user_info = Donor.objects.filter(user=self.request.user)

		if not check_user_info:
			return False
		return True