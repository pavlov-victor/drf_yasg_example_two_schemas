from django.urls import path, include

urlpatterns = [
    path('app_1/', include('app_1.doctor_urls')),
    path('app_2/', include('app_2.doctor_urls')),
]
