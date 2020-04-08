from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView
from django.db.models import Q
from .models import Donor, Patient, BloodRequest, DonorRequest
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import SearchDonorForm
from .send_sms import welcome_message, send_donation_request

def index(request):
	if request.method == 'POST':
		r_country = request.POST['country']
		r_blood_group = request.POST['blood_group']
		r_location = request.POST['location']


		country_donor_records = Donor.objects.filter(country=r_country)
		country_donor_records_total = country_donor_records.count()
		location_donor_records = country_donor_records.filter(Q(location1=r_location) | Q(location2=r_location))
		location_donor_records_total = location_donor_records.count()
		bloodgroup_donor_records = location_donor_records.filter(blood_group=r_blood_group)
		bloodgroup_donor_records_total = bloodgroup_donor_records.count()

		context = {
			'r_country' : r_country,
			'r_location' : r_location,
			'r_blood_group' : r_blood_group,
			'country_donor_records_total' : country_donor_records_total,
			'location_donor_records_total' : location_donor_records_total,
			'bloodgroup_donor_records_total' : bloodgroup_donor_records_total
		}

		return render(request, 'core/donorsearchresult.html', context)

	else:
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
		r_phone = form.cleaned_data['phone_number']
		r_name = form.cleaned_data['full_name']
		welcome_message(r_phone, r_name)
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


class addPatientInfo(LoginRequiredMixin, UserPassesTestMixin, CreateView):

	

	model = Patient
	fields = ['full_name','age', 'gender', 'phone_number']
	template_name = 'core/addpatientinfo.html'
	success_url = reverse_lazy('core:index')


		
	def form_valid(self, form):
		form.instance.user = self.request.user
		r_phone = form.cleaned_data['phone_number']
		r_name = form.cleaned_data['full_name']
		welcome_message(r_phone, r_name)
		return super().form_valid(form)


	def test_func(self):

		check_user_info = Patient.objects.filter(user=self.request.user)			
		if not check_user_info:
			return True
		return False

	def user_passes_test(self, request):
		if request.user.is_authenticated:
			check_user_info = Patient.objects.filter(user=self.request.user)

			if not check_user_info:
				return True
			return False

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			if not self.user_passes_test(request):
				user_profile = Patient.objects.filter(user=self.request.user)
				return redirect('core:update-patient-info', pk=user_profile[0].pk)
		return super(addPatientInfo, self).dispatch(
		    request, *args, **kwargs)

class updatePatientInfo(LoginRequiredMixin, UpdateView):
	model = Patient
	fields = ['full_name','age', 'gender', 'phone_number']
	template_name = 'core/updatepatientinfo.html'
	success_url = reverse_lazy('core:index')

	

	def user_passes_test(self, request):
		if request.user.is_authenticated:
		    self.object = self.get_object()
		    return self.object.user == request.user
		return False

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			user_profile = Patient.objects.filter(user=self.request.user)
			
			if not self.user_passes_test(request):
				if not user_profile:
					return redirect('core:add-patient-info')
				return redirect('core:update-patient-info', pk=user_profile[0].pk)
		return super(updatePatientInfo, self).dispatch(
	    request, *args, **kwargs)


class RequestBlood(LoginRequiredMixin, CreateView):
	model = BloodRequest
	fields = ['blood_group', 'phone_number', 'country', 'location1', 'location2', 'required_on']
	template_name = 'core/requestblood.html'
	success_url = reverse_lazy('core:index')

	def get_form(self):
		'''add date picker in forms'''
		from django.forms.widgets import SelectDateWidget
		form = super(RequestBlood, self).get_form()
		form.fields['required_on'].widget = SelectDateWidget()
		
		return form

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)


def HandleBloodRequest(request):
	user = request.user

	user_blood_request = BloodRequest.objects.filter(user=user)
	context={
		'user_blood_request' : user_blood_request,
	}
	
	return render(request, 'core/userbloodrequest.html', context)


def sendDonorRequest(request, pk):
	user = request.user
	request_data = BloodRequest.objects.get(pk=pk)
	

	req_bloodgroup = request_data.blood_group
	req_country = request_data.country
	req_location1 = request_data.location1
	req_location2 = request_data.location2
	req_required_on = request_data.required_on

	country_donor_records = Donor.objects.filter(country=req_country)
	country_donor_records_total = country_donor_records.count()
	location_donor_records = country_donor_records.filter(Q(location1=req_location1) | Q(location2=req_location2))
	location_donor_records_total = location_donor_records.count()
	matching_records = location_donor_records.filter(blood_group=req_bloodgroup)[:10]
	matching_records_total = matching_records.count()

	request_check = DonorRequest.objects.filter(bloodrequest=request_data)

	if not request_check:
	
		instance = DonorRequest.objects.create(bloodrequest=request_data)
		for record in matching_records:
			send_donation_request(record.phone_number, record.full_name, req_country, req_location1, req_bloodgroup)
			instance.user.add(record.user)



	context = {
			'req_country' : req_country,
			'req_location' : req_location1,
			'req_blood_group' : req_bloodgroup,
			'country_donor_records_total' : country_donor_records_total,
			'location_donor_records_total' : location_donor_records_total,
			'matching_records_total' : matching_records_total,
		}
	
	return render(request, 'core/myrequestdata.html', context)