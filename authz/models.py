from django.db import models
import uuid
from django.contrib.auth import get_user_model

User = get_user_model()

# Auth0 User
class Auth0User(models.Model):
    auth0_id = models.CharField(verbose_name="Auth0 ID", max_length=255, unique=True)
    # Relation with user django
    user = models.OneToOneField(User, verbose_name="Django User", on_delete=models.CASCADE, related_name='auth0user')
    # Auth0 Email
    email = models.EmailField(verbose_name="Auth0 Email", max_length=254)
    email_verified = models.BooleanField(verbose_name="Auth0 Email Verified", default=False)
    # Auth0 Role ??

    def __str__(self):
        return f"{self.email} - {self.id}  "

