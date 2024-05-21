from django.urls import path
from .views import err_404_view

app_name = "errhandlers"

urlpatterns = [
    path("404/", err_404_view, name="err_404_page"),
]
