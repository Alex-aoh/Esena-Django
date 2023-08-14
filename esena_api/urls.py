from django.urls import path, include

urlpatterns = [
    path("v1/", include("esena_api.api.v1.urls")),
        path("v2/", include("esena_api.api.v2.urls")),
]
