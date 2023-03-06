from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from . import doctor_urls
from . import patient_urls

config_admin = {
    'title': 'Doctor API',
    'description': 'API for doctor only',
    'default_version': 'v1',
}

config_user = {
    'title': 'User API',
    'description': 'API for authenticated users',
    'default_version': 'v1',
}

schema_view_admin = get_schema_view(
    openapi.Info(
        **config_admin,
    ),
    public=True,
    urlconf=doctor_urls
)

schema_view_user = get_schema_view(
    openapi.Info(
        **config_user,
    ),
    public=True,
    urlconf=patient_urls
)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^doctor-api/swagger(?P<format>\.json|\.yaml)$', schema_view_admin.without_ui(cache_timeout=0),
            name='schema-json-doctor'),
    re_path(r'^user-api/swagger(?P<format>\.json|\.yaml)$', schema_view_user.without_ui(cache_timeout=0),
            name='schema-json-user'),
    path('doctor-api/swagger/', schema_view_admin.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui-admin'),
    path('user-api/swagger/', schema_view_user.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui-user'),
    path('doctors/api/v1/', include('drf_example.doctor_urls')),
    path('patients/api/v1/', include('drf_example.patient_urls')),
]
