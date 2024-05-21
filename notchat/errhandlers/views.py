from django.shortcuts import render


def err_404_view(request, exception):
    return render(request, "errhandlers/err_404.html")
