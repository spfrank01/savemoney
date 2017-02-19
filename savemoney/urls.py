from django.conf.urls import url

from . import views

app_name = 'savemoney'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^(?P<pk>[0-9]+)/$', views.IndexView.as_view(), name='index'),
    url(r'^detail/$', views.detail, name='detail'),
]
