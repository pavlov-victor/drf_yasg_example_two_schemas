from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def hello_api_user(request):
    return Response({'hello': 'user'})


@api_view()
def hello_api_doctor(request):
    return Response({'hello': 'doctor'})
