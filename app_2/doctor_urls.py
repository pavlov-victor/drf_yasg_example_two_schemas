from django.urls import path

from .views import second_api_doctor

urlpatterns = [
    path('second_doctor', second_api_doctor)
]
