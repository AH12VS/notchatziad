from django.urls import path
from .views import signout_view

app_name = "signout"

urlpatterns = [
    path("", signout_view, name="signout_page"),
]
