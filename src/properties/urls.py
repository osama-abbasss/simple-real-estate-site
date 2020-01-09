from django.urls import path
from . import views

app_name = 'properties'

urlpatterns = [
    path('', views.properties_view, name='properties'),
    path('<slug>/', views.PropertyDetailView.as_view(), name='property_detail'),
    path('reserve/property/', views.reserve_property, name='reserve')
]
