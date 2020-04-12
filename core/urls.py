from django.urls import path
from .views import (index,
        addDonnorInfo, 
        updateDonnorInfo, 
        addPatientInfo, 
        updatePatientInfo, 
        RequestBlood,
        HandleBloodRequest,
        sendDonorRequest,
        donationRequests,
        userDonate,
    )

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),

    path('donr-register', index, name='regdonor'),
    path('add-donor-info', addDonnorInfo.as_view(), name='add-donor-info'),
    path('update-donor-info/<int:pk>', updateDonnorInfo.as_view(), name='update-donor-info'),
    path('add-patient-info', addPatientInfo.as_view(), name='add-patient-info'),
    path('update-patient-info/<int:pk>', updatePatientInfo.as_view(), name='update-patient-info'),
    path('request-blood-donation', RequestBlood.as_view(), name='request-blood-donation'),
    path('my-requests',HandleBloodRequest, name='my-requests'),
    path('send-request/<int:pk>', sendDonorRequest, name='send-request'),
    path('donation-requests', donationRequests.as_view(), name='donation-requests'),
    path('user-donate/<int:pk>', userDonate, name='user-donate'),


]