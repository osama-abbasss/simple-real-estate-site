from django.urls import path
from . import views

app_name = 'agents'

urlpatterns = [
    path('', views.agents_list_view, name='agents'),
    path('<slug>', views.AgentDetailView.as_view(), name='agent_detail'),
]
