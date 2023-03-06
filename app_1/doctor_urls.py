from django.urls import path

from .views import hello_api_doctor

urlpatterns = [
    path('hello_doctor', hello_api_doctor)
]
