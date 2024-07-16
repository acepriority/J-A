from rest_framework import viewsets
from .models import Person, LandLord, Tenant
from .serializers import PersonSerializer, LandLordSerializer, TenantSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class LandLordViewSet(viewsets.ModelViewSet):
    queryset = LandLord.objects.all()
    serializer_class = LandLordSerializer


class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
