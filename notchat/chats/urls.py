from django.urls import path
from .views import chats_view, chat_view

app_name = "chats"

urlpatterns = [
    path("", chats_view, name="chats_page"),
    path("chat/", chat_view, name="chat_page"),
]
