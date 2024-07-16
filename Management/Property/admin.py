from django.contrib import admin
from .models import Person, LandLord, Tenant

admin.site.register(Person)
admin.site.register(LandLord)
admin.site.register(Tenant)
