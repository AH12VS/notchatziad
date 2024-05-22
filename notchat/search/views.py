from django.shortcuts import render
from rooms.models import RoomModel
from django.db.models import Q


def search_view(request):
    context = {}
    if request.method == "GET":
        q = request.GET.get("q")
        if q:
            request.session["query_session_var"] = q
        else:  # this else is used when the q is empty so we try to get it from sessions
            try:
                q = request.session["query_session_var"]
            except:
                q = ""

        rooms = RoomModel.objects.filter(Q(name__icontains=q) | Q(desc__icontains=q))

        context = {
            "rooms": rooms,
        }

    return render(request, "search/search.html", context)
