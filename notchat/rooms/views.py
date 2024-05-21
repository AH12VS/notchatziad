from django.shortcuts import render, redirect, get_object_or_404
from .models import RoomModel, MessageModel


def rooms_view(request):
    if not request.user.is_authenticated:
        return redirect("home:home_page")

    rooms = RoomModel.objects.all()

    context = {
        "rooms": rooms,
    }

    return render(request, "rooms/rooms.html", context)


def room_view(request, slug):
    if not request.user.is_authenticated:
        return redirect("home:home_page")

    room = get_object_or_404(RoomModel, slug=slug)
    # messages = room.messages[0:30]
    messages = MessageModel.objects.filter(room=room)

    context = {
        "room": room,
        "messages": messages
    }

    return render(request, "rooms/room.html", context)
