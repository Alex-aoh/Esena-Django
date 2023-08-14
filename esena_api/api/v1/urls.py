from django.urls import path, include
from . import views
urlpatterns = [
    path("usernames/check-available", views.UsernamesCheckAvailable.as_view(), name="usernames-check-available"),
    path("emails/check-available", views.EmailsCheckAvailable.as_view(), name="emails-check-available"),
]
