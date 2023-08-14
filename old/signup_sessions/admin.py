from django.contrib import admin
from . import models

admin.site.register(models.SignUpSession)
admin.site.register(models.UsernameSignUpSession)
admin.site.register(models.EmailSignUpSession)
admin.site.register(models.PasswordSignUpSession)