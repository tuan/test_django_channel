from django.http import HttpRequest
from django.shortcuts import render


async def index(request: HttpRequest):
    return render(request, "home/home.html")


async def room(request: HttpRequest, room_name):
    return render(request, "home/room.html", {"room_name": room_name})
