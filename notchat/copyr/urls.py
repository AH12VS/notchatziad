from django.urls import path
from .views import copyr_view

app_name = "copyr"

urlpatterns = [
    path("", copyr_view, name="copyr_page"),
]

