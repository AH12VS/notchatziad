from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import AccountForm
from django.contrib import messages


def account_view(request):
    if not request.user.is_authenticated:
        return redirect("home:home_page")

    form = AccountForm()
    if request.method == "POST":
        form = AccountForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            user = request.user
            user.username = cd["username"]
            passwd = cd["passwd"]
            confirm_passwd = cd["confirm_passwd"]

            if str(passwd) == str(confirm_passwd):
                user.set_password(passwd)

            if cd["img_prof"] != None:
                user.img_prof = cd["img_prof"]

            user.save()

            user = authenticate(request, email=user.email, password=passwd)
            login(request, user)

            messages.success(request, "Account Changed Successfully")
            return redirect("home:home_page")

        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)

    return render(request, "users/account.html")
