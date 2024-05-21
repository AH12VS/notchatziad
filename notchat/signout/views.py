from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib import messages


def signout_view(request):
    if not request.user.is_authenticated:
        return redirect("home:home_page")

    logout(request)

    messages.success(request, "Signed Out Successfully")

    return redirect("home:home_page")
