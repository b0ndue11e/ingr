"""ingr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from ingr.views import index, weapon, history, contacts
from mods.views import mods_list
from events.views import event_list
from weapon.views import weapons_list


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^event/$', event_list),
    url(r'^mods/$', mods_list),
    url(r'^weapon/$', weapons_list),
    url(r'^history/$', history),
    url(r'^contacts/$', contacts),
]
