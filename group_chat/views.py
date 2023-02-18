from django.shortcuts import render, redirect
from .models import Room, RoomMessage
from .forms import RoomForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def roomChat(request, room_name):
    now = datetime.datetime.now()
    room = Room.objects.get(room_name=room_name)
    messages = RoomMessage.objects.filter(room=room)
    return render(request, "room.html", {"room_name": room_name,"messages":messages,"now":now})
