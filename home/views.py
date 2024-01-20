from django.http import HttpRequest
from django.shortcuts import render


async def index(request: HttpRequest):
    return render(request, "home/home.html")
