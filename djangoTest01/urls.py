from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoTest01.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^djangotest/', include('djangoTestApp01.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
