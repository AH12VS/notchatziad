from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

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
    path("users/", include("users.urls", "users")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
