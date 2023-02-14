from django.shortcuts import render, redirect
from .models import Room, RoomMessage
from .forms import RoomForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def roomChat(request, room_name):
    return render(request, "room.html", {"room_name": room_name})
