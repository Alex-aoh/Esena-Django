from django.urls import include, path
from .views import *
urlpatterns = [
    path("", requestTokenView, name="main-view"),
]
