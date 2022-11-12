from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def group_posts(request, slug):
    return HttpResponse(f"Групповые посты {slug}")


def index(request):
    return HttpResponse("Главная страница")
