from django.conf.urls.defaults import patterns


urlpatterns = patterns('apps.control.views',
    (r'^$', 'index'),
)
