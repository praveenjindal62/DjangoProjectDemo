from django.conf.urls import patterns, include, url
from django.contrib import admin
from polls import views
urlpatterns = patterns('',
 	url(r'^polls/', include('polls.urls',namespace="polls")),
 	url(r'^user/', include('userReg.urls',namespace="userReg")),
    url(r'^admin/', include(admin.site.urls)),


)
