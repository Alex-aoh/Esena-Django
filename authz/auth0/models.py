from django.db import models

class Auth0ManagementApiToken(models.Model):
    token = models.CharField(verbose_name="Token", max_length=10000)
    updated = models.DateTimeField(verbose_name="Updated at", auto_now=True)

# class RoleId(models.Model):
#     name= models.CharField(verbose_name="Name", max_length=50)
#     role_id = models.CharField(verbose_name="Role ID", max_length=150)

#     def __str__(self) -> str:
#         return f'{self.name} | {self.role_id}'