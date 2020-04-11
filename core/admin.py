from django.contrib import admin
from core.models import *

# Register your models here.
admin.site.register(Donor)
admin.site.register(Patient)
admin.site.register(BloodRequest)
admin.site.register(DonorRequest)
admin.site.register(DonorAccept)