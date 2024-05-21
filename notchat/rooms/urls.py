from django.urls import path
from .views import rooms_view, room_view

app_name = "rooms"

urlpatterns = [
    path("", rooms_view, name="rooms_page"),
    path("room/<slug>", room_view, name="room_page"),
]
