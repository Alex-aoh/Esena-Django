from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', include("authz.urls")),
    path('api/', include("esena_api.urls")),
    path('api/', include("accounts.api.urls")),
    path('api/', include("social_profiles.api.urls")),
]
