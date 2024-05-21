from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls", "home")),
    path("signin/", include("signin.urls", "signin")),
    path("signout/", include("signout.urls", "signout")),
    path("signup/", include("signup.urls", "signup")),
]
