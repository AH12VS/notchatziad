from django.shortcuts import render, redirect


def rooms_view(request):
    if not request.user.is_authenticated:
        return redirect("home:home_page")

    return render(request, "rooms/rooms.html")


def room_view(request):
    if not request.user.is_authenticated:
        return redirect("home:home_page")

    return render(request, "rooms/room.html")
