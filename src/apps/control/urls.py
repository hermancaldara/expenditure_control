from django.conf.urls.defaults import patterns


urlpatterns = patterns('apps.control.views',
    (r'^$', 'index'),
    (r'^expense_saved/$', 'expense_saved'),
    (r'^expenses/$', 'all_expenses'),
)