from django.conf.urls import url

from .views import HomeView, URLRedirectView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='short'),
    url(r'^(?P<shortcode>[\w-]+)/$', URLRedirectView.as_view(), name='scode'),
]
