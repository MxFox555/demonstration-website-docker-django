from django.urls import path
from . import views

app_name = 'web'
urlpatterns = [
    path('home/', views.panel_dashboard, name='panel_dashboard'),
    path('key/', views.panel_key, name='panel_key'),
    path('tutorial/', views.panel_tutorial, name='panel_tutorial'),
    path('app/', views.panel_app, name='panel_app'),
    path('settings/', views.panel_settings, name='panel_settings'),
    path('delete/', views.delete_account, name='delete_account'),
]