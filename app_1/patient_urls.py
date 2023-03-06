from django.urls import path

from .views import hello_api_user

urlpatterns = [
    path('hello_user', hello_api_user)
]
