from django.urls import path
from .views import login, logout

urlpatterns = [
    path("users/login", login),
    path("users/logout", logout),
]
