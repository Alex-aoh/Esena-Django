from django.contrib import admin
from .models import Auth0User
from .auth0.models import Auth0ManagementApiToken
# Register your models here.
admin.site.register(Auth0User)
admin.site.register(Auth0ManagementApiToken)
