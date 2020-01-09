from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('', views.about_us_view, name='about'),
    path('<slug>', views.BolgDetailView.as_view(), name='blog_detail'),
]
