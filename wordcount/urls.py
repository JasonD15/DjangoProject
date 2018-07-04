"""wordcount URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
#from file import method
from django.urls import path    #path function creates a URL/(webpage linked to an address string)
from wordcount.views import *


urlpatterns = [
    path('',home, name='home'),
    path('count/',count, name='count'),
    path('about/',about, name='about'),
]
#e.g. path('countnigga',count, name='count') creates a url = http://127.0.0.1:8000/countnigga which is linked to count.html page.