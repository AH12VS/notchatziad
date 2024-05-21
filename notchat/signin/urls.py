from django.urls import path
from .views import signin_view

app_name = "signin"

urlpatterns = [
    path("", signin_view, name="signin_page"),
]
