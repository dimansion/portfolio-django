from django.conf.urls import patterns, url
from .views import (
	home_view
	)


urlpatterns =[
        url(r'^$', home_view, name='home'),
]

