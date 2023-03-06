from django.urls import path

from .views import second_api_user

urlpatterns = [
    path('second_user', second_api_user)
]
