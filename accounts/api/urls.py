from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("v1/accounts/my-account", views.MyAccount.as_view(), name="accounts-my-account"),
]
