from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf import settings
from mods.views import mods_list
from weapon.views import weapons_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^mods/$', mods_list),
    url(r'^weapon/$', weapons_list),
    url(r'^history/$', views.history),
    url(r'^contacts/$', views.contacts),
    url(r'^events/$', views.events),
    url(r'^events/', include('events.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]
