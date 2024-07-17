from django.db import models


class Person(models.Model):
    first_name = models.CharField(
        max_length=100
        )
    last_name = models.CharField(
        max_length=100
        )
    telephone = models.IntegerField(
        unique=True
        )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class LandLord(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        related_name='landlord'
        )

    def __str__(self):
        return f"LandLord: {self.person}"


class Property(models.Model):
    location = models.CharField(
        max_length=255
        )
    landlord = models.ForeignKey(
        LandLord,
        on_delete=models.CASCADE,
        related_name='properties'
        )

    def __str__(self):
        return f"Property: {self.location}, Landlord: {self.landlord}"


class House(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='houses')
    name = models.CharField(
        max_length=100
        )
    rent = models.IntegerField()
    tenant = models.ForeignKey(
        'Tenant',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='houses')

    def __str__(self):
        return f"House: {self.name}, Property: {self.property}"


class Tenant(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        related_name='tenant')
    landlord = models.ForeignKey(
        LandLord,
        on_delete=models.CASCADE,
        related_name='tenants')

    def __str__(self):
        return f"Tenant: {self.person}"
