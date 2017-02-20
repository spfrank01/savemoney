from django.conf.urls import url

from . import views

app_name = 'SaveMoney'
urlpatterns = [
    url(r'^$', views.detail, name='detail'),
	url(r'^(?P<page>[0-9]+)/$', views.detail, name='detail'),
	url(r'^save/$',views.save, name='save'),
	url(r'^(?P<page>[0-9]+)/olderPage/$', views.olderPage, name='olderPage'),
	url(r'^(?P<page>[0-9]+)/newerPage/$', views.newerPage, name='newerPage'),
]
