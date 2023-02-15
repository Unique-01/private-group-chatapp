from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.indexView, name="index"),
    path("group/", include("group_chat.urls")),
    path("private/", include("private_chat.urls")),
    path("accounts/", include("allauth.urls")),
]
