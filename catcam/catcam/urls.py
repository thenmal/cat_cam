from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ccam.views.index', name='index'),
    url(r'^stay_alive$', 'ccam.views.stay_alive', name='stay_alive'),
    url(r'^right$', 'ccam.views.right', name='right'),
    url(r'^left$', 'ccam.views.left', name='left'),
    # url(r'^catcam/', include('catcam.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
