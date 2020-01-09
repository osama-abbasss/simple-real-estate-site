from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('about/', include('about.urls', namespace='about')),
    path('agents/', include('agents.urls', namespace='agents')),
    path('properties/', include('properties.urls', namespace='properties')),
    path('', include('searches.urls', namespace='searches')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
