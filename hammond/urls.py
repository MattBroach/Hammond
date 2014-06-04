from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from grid import views

#For Development static files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hammond.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r"^$",views.index,name="index"),
    url(r'^main/',views.main,name="main")
)  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
