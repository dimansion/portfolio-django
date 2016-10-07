from django.conf.urls import patterns, url
from .views import (
	list_jadwal,
	hapus_jadwal,
	)


urlpatterns =[
    url(r'^$', list_jadwal, name='list_jadwal'),
    url(r'^jadwal/(?P<pk>[0-9]+)/hapus/$', hapus_jadwal, name='hapus_jadwal'),
]
