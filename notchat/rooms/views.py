from django.shortcuts import render, redirect
from .models import RoomModel


def rooms_view(request):
    if not request.user.is_authenticated:
        return redirect("home:home_page")

    rooms = RoomModel.objects.all()

    context = {
        "rooms": rooms,
    }

    return render(request, "rooms/rooms.html", context)


def room_view(request):
    if not request.user.is_authenticated:
        return redirect("home:home_page")

    return render(request, "rooms/room.html")
