from django.shortcuts import render,redirect
from group_chat.models import Room
from group_chat.forms import RoomForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def indexView(request):
    availableRoom = Room.objects.all()
    availableUser = User.objects.all()
    roomForm = RoomForm

    if request.method == "POST":
        roomForm = RoomForm(request.POST)
        if roomForm.is_valid():
            form = roomForm.save(commit=False)
            form.admin = request.user
            form.save()
            return redirect("index")

            messages.success(request, "Room has been created successfuly")
    return render(
        request,
        "index.html",
        {
            "availableRoom": availableRoom,
            "roomForm": roomForm,
            "availableUser": availableUser,
        },
    )
