from django.conf.urls import url

from . import views

app_name = 'SaveMoney'
urlpatterns = [
    url(r'^$', views.detail, name='detail'),
	url(r'^(?P<page>[0-9]+)/$', views.detail, name='detail'),
	url(r'^saveDatailtoModel/$',views.saveDatailtoModel, name='saveDatailtoModel'),
	url(r'^(?P<page>[0-9]+)/olderPage/$', views.olderPage, name='olderPage'),
	url(r'^(?P<page>[0-9]+)/newerPage/$', views.newerPage, name='newerPage'),
	url(r'^downloadcsv/$', views.downloadCSVFile, name='downloadCSVFile'),
	url(r'^savecsv/$', views.saveCSVFile, name='saveCSVFile'),
]
