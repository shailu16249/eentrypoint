"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin


from profiles import views as profiles_views
from contact import views as contact_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', profiles_views.home, name='home'),
    path('engineering/', profiles_views.engineering, name='engineering'),
    path('medical/', profiles_views.medical, name='medical'),
    path('ssc/', profiles_views.ssc, name='ssc'),
    path('state_exam/', profiles_views.state_exam, name='state_exam'),
    path('upsc/', profiles_views.upsc, name='upsc'),
    path('about/', profiles_views.about, name='about'),
    path('tet/', profiles_views.tet, name='tet'),
    path('profile/', profiles_views.userProfile, name='profile'),
    path('contact/', contact_views.contact, name='contact'),
    path('accounts/', include('allauth.urls')),

]     

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)	
