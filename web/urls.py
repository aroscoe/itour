from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # url(r'^$', 'views.index', name="home"),
    url(r'^([0-9\-]+/[0-9\-]+)?/?$', 'views.index', name="home"),
)
