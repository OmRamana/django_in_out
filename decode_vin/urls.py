"""decode_vin URL Configuration

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
from django.contrib import admin
from django.urls import path
from vin_decoder.views import GetDroplets
from vin_decoder.views import OriginalDroplets
from vin_decoder.views import VinFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', GetDroplets.as_view(template_name='index.html'), name='Droplet View'),
    path('drop/',OriginalDroplets.as_view(template_name='droplets.html'), name ='OriginalDroplets'),
    path('form/',VinFormView.as_view(template_name='index.html'), name="Form"),
]
