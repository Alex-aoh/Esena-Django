from django.db import models
from authz.models import Auth0User


# Esena Account
class Account(models.Model):
    # Auth0user relation one to one
    auth0user = models.OneToOneField(Auth0User, verbose_name="Auth0User", on_delete=models.CASCADE)

    first_name = models.CharField(verbose_name="First Name", max_length=50, blank=True)
    last_name = models.CharField(verbose_name="Last Name", max_length=50, blank=True)
    # phone_number

    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]

    gender = models.CharField(verbose_name="Gender", max_length=1, choices=GENDER_CHOICES, blank=True, default="O")

    birthday = models.DateTimeField(verbose_name="Birthday", null=True, blank=True)

    management_registered = models.BooleanField(verbose_name="Management registered", default=False)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} - {self.id}"
