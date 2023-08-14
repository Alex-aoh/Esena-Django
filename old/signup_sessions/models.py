from django.db import models

# Create your models here.
class SignUpSession(models.Model):
    auth0user = models.OneToOneField("authz.Auth0User", verbose_name="Auth0User", on_delete=models.CASCADE)
    updated_at = models.DateTimeField(verbose_name="Updated At", auto_now=True)
    created_at = models.DateTimeField(verbose_name="Updated At", auto_now_add=True)

    def __str__(self):
        return f"{self.pk} - {self.auth0user.email}"
    

class UsernameSignUpSession(models.Model):
    signup_session = models.OneToOneField(SignUpSession, verbose_name="SignUp Session", on_delete=models.CASCADE)
    username = models.CharField(verbose_name="Username", max_length=15, unique=True)
    updated_at = models.DateTimeField(verbose_name="Updated At", auto_now=True)
    def __str__(self):
        return f"{self.pk} - {self.username} - {self.signup_session.auth0user.email}"

class EmailSignUpSession(models.Model):
    signup_session = models.OneToOneField(SignUpSession, verbose_name="SignUp Session", on_delete=models.CASCADE)
    email = models.CharField(verbose_name="Email", max_length=320, unique=True)
    updated_at = models.DateTimeField(verbose_name="Updated At", auto_now=True)
    def __str__(self):
        return f"{self.pk} - {self.username} - {self.signup_session.auth0user.email}"

class PasswordSignUpSession(models.Model):
    signup_session = models.OneToOneField(SignUpSession, verbose_name="SignUp Session", on_delete=models.CASCADE)
    password = models.CharField(verbose_name="Password", max_length=150)
    updated_at = models.DateTimeField(verbose_name="Updated At", auto_now=True)
    def __str__(self):
        return f"{self.pk} - {self.username} - {self.signup_session.auth0user.email}"
