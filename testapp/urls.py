from django.conf.urls import handler404, handler500, include, url
from django.contrib import admin
from django.contrib.auth.views import logout

__all__ = ['handler404', 'handler500']


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^metric/', include('metric.urls', namespace="metric")),
]