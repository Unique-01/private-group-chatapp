from django.shortcuts import render
from .models import PrivateMessage


def privateChat(request, username):
    return render(request, "privatechat.html", {"username": username})
