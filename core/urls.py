from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from core import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Celebi API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.celebi.com/policies/terms/",
        contact=openapi.Contact(email="contact@celebi.local"),
        license=openapi.License(name="Celebi License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('super/user/', admin.site.urls),

    path('auth/', include('account.api.urls')),
    path('media/', include('media.api.urls')),
    path('hotel/', include('hotel.api.urls'), name='hotel'),
    path('restaurant/', include('restaurant.api.urls'), name='restaurant'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path('api-auth/',include('rest_framework.urls')), # browsable için
    # path('api/rest-auth/',include('rest_auth.urls')), # dajngo rest auth için ednpointler

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
