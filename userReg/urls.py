from django.conf.urls import patterns, url
from userReg import views

urlpatterns = patterns('',
    url(r'^$', views.NewUser, name='index'),
    url(r'^getdetail$',views.GetDetail,name='gdetail'),
    url(r'^userdetail/(?P<user_id>\d+)$', views.result, name='result'),    
)