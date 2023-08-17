from django.urls import path, include
from .views import MySocialProfile
from rest_framework import routers


urlpatterns = [
    path("v1/social-profiles/follows/", include("social_profiles.services.follows.urls")),
    path("v1/social-profiles/my-social-profile/", MySocialProfile.as_view(), name="my-social-profile")
]

# urlpatterns += router.urls
