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


class Tenant(models.Model):
    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        related_name='tenant'
        )
    landlord = models.ForeignKey(
        LandLord,
        on_delete=models.CASCADE
        )
    house_id = models.CharField(
        max_length=100,
        unique=True
        )
    rent = models.IntegerField()

    def __str__(self):
        return f"Tenant: {self.person}, House ID: {self.house_id}"
