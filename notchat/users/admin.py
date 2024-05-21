from django.contrib import admin
from users.models import UserModel


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    ordering = ("-date_joined",)
    list_display = (
        "email",
        "username",
        "date_joined",
        "is_active",
        "updated",
        "last_login",
    )
    list_editable = ("is_active",)
    list_filter = (
        "last_login",
        "is_active",
        "is_staff",
        "is_admin",
        "is_superuser",
    )
    search_fields = (
        "email",
        "username",
    )
