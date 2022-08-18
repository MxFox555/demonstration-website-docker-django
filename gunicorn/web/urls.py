import imp
from django.urls import path
from web import views
from django.contrib.sitemaps.views import sitemap
#from web.sitemaps import Static_Sitemap

#sitemaps = {
#    'static': Static_Sitemap,
#}

#app_name = 'web'
'''urlpatterns = [
    path('home/', views.landing, name='landing'),
    path('about/', views.about, name='about'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
    path('privacypolicy/', views.privacypolicy, name='privacypolicy'),
    path('termsofservice/', views.termsofservice, name='termsofservice'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.pagelogin, name='login'),
    path('logout/', views.pagelogout, name='logout'),
    path('forgotpassword/', views.pageforgotpassword, name='forgotpassword'),
    path('resetpassword/<str:key>/', views.pageresetpassword, name='resetpassword'),
    path('activate/<str:key>/', views.pageactivate, name='activate'),
    #path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]'''