from rest_framework import serializers
from .models import Person, LandLord, Tenant


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class LandLordSerializer(serializers.ModelSerializer):
    person = PersonSerializer()

    class Meta:
        model = LandLord
        fields = '__all__'


class TenantSerializer(serializers.ModelSerializer):
    person = PersonSerializer()

    class Meta:
        model = Tenant
        fields = '__all__'
