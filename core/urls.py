from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),

    path('donr-register', index, name='regdonor'),
    path('searchresult', index, name='searchresult'),
    path('donorlist', index, name='donorlist'),
 #   path('add-record', views.addrecord, name='addrecord'),
    path('contact', index, name='contact'),
    path('donor-confirmation', index, name='donorconf'),
    path('pending-donors', index, name='pendingdonors'),
    path('donor/<int:pk>/update', index, name='donor-update'),
    path('blood-register', index, name='bloodregister'),
    path('search-blood', index, name='searchblood'),
    path('search-donor',index, name='searchdonor'),
]