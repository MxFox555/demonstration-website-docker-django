"""stockinterestmetric URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.views.generic.base import RedirectView, TemplateView
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from web.sitemaps import Static_Sitemap
from django.urls import reverse
import web.views as web_views

sitemaps = {
    'static': Static_Sitemap,
}

urlpatterns = [
    path('panel/admin/', admin.site.urls, name='panel-admin'),
    path('panel/', include('loggedin.urls')),
    path('api/', include('api.urls')),
    path('', RedirectView.as_view(url='/home/', permanent=False)),
    #path('', include('web.urls'), name='web'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),

    #For the 'web' app
    path('home/', web_views.landing, name='landing'),
    path('features/', web_views.pricing, name='pricing'),
    path('contact/', web_views.contact, name='contact'),
    path('privacypolicy/', web_views.privacypolicy, name='privacypolicy'),
    path('termsofservice/', web_views.termsofservice, name='termsofservice'),
    path('signup/', web_views.signup, name='signup'),
    path('login/', web_views.pagelogin, name='login'),
    path('logout/', web_views.pagelogout, name='logout'),
    path('forgotpassword/', web_views.pageforgotpassword, name='forgotpassword'),
    path('resetpassword/<str:key>/', web_views.pageresetpassword, name='resetpassword'),
    path('activate/<str:key>/', web_views.pageactivate, name='activate'),
]