from django.contrib import admin
from django.urls import path, include

handler404 = "errhandlers.views.err_404_view"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls", "home")),
    path("signin/", include("signin.urls", "signin")),
    path("signout/", include("signout.urls", "signout")),
    path("signup/", include("signup.urls", "signup")),
    path("about/", include("about.urls", "about")),
    path("copyr/", include("copyr.urls", "copyr")),
    path("err/", include("errhandlers.urls", "errhandlers")),
    path("chats/", include("chats.urls", "chats")),
]
