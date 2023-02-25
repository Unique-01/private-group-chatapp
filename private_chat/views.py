from django.shortcuts import render
from .models import PrivateMessage
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def privateChat(request, username):
    user1 = request.user.username
    user2 = username
    user_list = [user1, user2]
    user_list.sort()
    user_list = "".join(user_list)

    now = datetime.datetime.now()
    messages = PrivateMessage.objects.filter(room=user_list)
    return render(request, "privatechat.html", {"username": username,"messages":messages,"now":now})
