from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexView,name='index'),
    path('<str:room_name>/',views.roomChat,name='room')
]