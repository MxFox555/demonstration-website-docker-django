from django.urls import path
from . import views

app_name = 'web'
urlpatterns = [
    path('request/', views.api_request, name='api_request'),
]