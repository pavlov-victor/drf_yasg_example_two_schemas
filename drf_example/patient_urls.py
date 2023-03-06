from django.urls import path, include

urlpatterns = [
    path('app_1/', include('app_1.patient_urls')),
    path('app_2/', include('app_2.patient_urls')),
]
