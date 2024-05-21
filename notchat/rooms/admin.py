from django.contrib import admin
from .models import RoomModel


@admin.register(RoomModel)
class RoomModelAdmin(admin.ModelAdmin):
    ordering = (
        "-created",
        "-name",
    )
    list_display = (
        "__str__",
        "name",
        "created",
        "desc",
    )
    list_editable = (
        "name",
        "desc",
    )
    list_filter = (
        "name",
        "created",
    )
    search_fields = (
        "name",
        "desc",
    )
