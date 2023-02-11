from django.shortcuts import render,redirect
from .models import Room,RoomMessage
from .forms import RoomForm
from django.contrib import messages

# Create your views here.

def indexView(request):
    availableRoom = Room.objects.all()
    roomForm = RoomForm

    if request.method == 'POST':
        roomForm=RoomForm(request.POST)
        if roomForm.is_valid():
            form = roomForm.save(commit=False)
            form.admin = request.user
            form.save()
            return redirect('index')

            messages.success(request, "Room has been created successfuly")
    return render(request, "index.html",{"availableRoom":availableRoom,"roomForm":roomForm})

def roomChat(request,room_name):
    return render(request, 'room.html')



    
