from django.shortcuts import render, redirect


def chats_view(request):
    if not request.user.is_authenticated:
        return redirect("home:home_page")

    return render(request, "chats/chats.html")


def chat_view(request):
    if not request.user.is_authenticated:
        return redirect("home:home_page")

    return render(request, "chats/chat.html")
