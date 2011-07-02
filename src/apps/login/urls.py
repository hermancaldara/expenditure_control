from django.conf.urls.defaults import *


urlpatterns = patterns('apps.login.views',
    (r'^$', 'index'),
)
