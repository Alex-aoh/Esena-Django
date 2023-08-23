from django.urls import path
from .views import *


urlpatterns = [
    # Endpoint for follow, unfollow, reject, acept, block, unblock, 
    path('follow-unfollow', FollowUnfollowView.as_view()),
]