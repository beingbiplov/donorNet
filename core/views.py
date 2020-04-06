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
	fields = ['full_name','age', 'gender', 'phone_number', 'blood_group', 'country', 'location1', 'location2','last_donated']
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

	def user_passes_test(self, request):
		if request.user.is_authenticated:
			check_user_info = Donor.objects.filter(user=self.request.user)

			if not check_user_info:
				return True
			return False

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			if not self.user_passes_test(request):
				user_profile = Donor.objects.filter(user=self.request.user)
				return redirect('core:update-donor-info', pk=user_profile[0].pk)
		return super(addDonnorInfo, self).dispatch(
		    request, *args, **kwargs)


class updateDonnorInfo(LoginRequiredMixin, UpdateView):
	model = Donor
	fields = ['full_name','age', 'gender', 'phone_number', 'blood_group', 'country', 'location1', 'location2', 'can_donate','last_donated']
	template_name = 'core/updatedonorinfo.html'
	success_url = reverse_lazy('core:index')

	

	def user_passes_test(self, request):
		if request.user.is_authenticated:
		    self.object = self.get_object()
		    return self.object.user == request.user
		return False

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			user_profile = Donor.objects.filter(user=self.request.user)
			
			if not self.user_passes_test(request):
				if not user_profile:
					return redirect('core:add-donor-info')
				return redirect('core:update-donor-info', pk=user_profile[0].pk)
		return super(updateDonnorInfo, self).dispatch(
	    request, *args, **kwargs)